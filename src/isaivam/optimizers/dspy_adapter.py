import typing as t

from isaivam.dataset_schema import SingleMetricAnnotation
from isaivam.llms.base import BaseIsaivamLLM
from isaivam.losses import Loss
from isaivam.prompt.pydantic_prompt import PydanticPrompt


def setup_dspy_llm(dspy: t.Any, isaivam_llm: BaseIsaivamLLM) -> None:
    """
    Configure DSPy to use Isaivam LLM.

    Parameters
    ----------
    dspy : Any
        The DSPy module.
    isaivam_llm : BaseIsaivamLLM
        Isaivam LLM instance to use for DSPy operations.
    """
    from isaivam.optimizers.dspy_llm_wrapper import IsaivamDSPyLM

    lm = IsaivamDSPyLM(isaivam_llm)
    dspy.settings.configure(lm=lm)


def pydantic_prompt_to_dspy_signature(
    prompt: PydanticPrompt[t.Any, t.Any],
) -> t.Type[t.Any]:
    """
    Convert Isaivam PydanticPrompt to DSPy Signature.

    Parameters
    ----------
    prompt : PydanticPrompt
        The Isaivam prompt to convert.

    Returns
    -------
    Type[dspy.Signature]
        A DSPy Signature class.
    """
    try:
        import dspy
    except ImportError as e:
        raise ImportError(
            "DSPy optimizer requires dspy-ai. Install with:\n"
            "  uv add 'isaivam[dspy]'  # or: pip install 'isaivam[dspy]'\n"
        ) from e

    fields = {}

    for name, field_info in prompt.input_model.model_fields.items():
        fields[name] = dspy.InputField(
            desc=field_info.description or "",
        )

    for name, field_info in prompt.output_model.model_fields.items():
        fields[name] = dspy.OutputField(
            desc=field_info.description or "",
        )

    signature_class = type(
        f"{prompt.__class__.__name__}Signature",
        (dspy.Signature,),
        {"__doc__": prompt.instruction, **fields},
    )

    return signature_class


def isaivam_dataset_to_dspy_examples(
    dataset: SingleMetricAnnotation,
    prompt_name: str,
) -> t.List[t.Any]:
    """
    Convert Isaivam annotated dataset to DSPy examples.

    Parameters
    ----------
    dataset : SingleMetricAnnotation
        The annotated dataset with ground truth scores.
    prompt_name : str
        The name of the prompt to extract examples for.

    Returns
    -------
    List[dspy.Example]
        List of DSPy examples for training.
    """
    try:
        import dspy
    except ImportError as e:
        raise ImportError(
            "DSPy optimizer requires dspy-ai. Install with:\n"
            "  uv add 'isaivam[dspy]'  # or: pip install 'isaivam[dspy]'\n"
        ) from e

    examples = []

    for sample in dataset:
        if not sample["is_accepted"]:
            continue

        prompt_data = sample["prompts"].get(prompt_name)

        if prompt_data is None:
            continue

        prompt_input = prompt_data["prompt_input"]
        prompt_output = (
            prompt_data["edited_output"]
            if prompt_data["edited_output"]
            else prompt_data["prompt_output"]
        )

        example_dict = {**prompt_input}
        if isinstance(prompt_output, dict):
            example_dict.update(prompt_output)
        else:
            example_dict["output"] = prompt_output

        input_keys = list(prompt_input.keys())
        example = dspy.Example(**example_dict).with_inputs(*input_keys)
        examples.append(example)

    return examples


def create_dspy_metric(
    loss: Loss, metric_name: str
) -> t.Callable[[t.Any, t.Any], float]:
    """
    Convert Isaivam Loss function to DSPy metric.

    DSPy expects a metric function with signature: metric(example, prediction) -> float
    where higher is better.

    Parameters
    ----------
    loss : Loss
        The Isaivam loss function.
    metric_name : str
        Name of the metric being optimized.

    Returns
    -------
    Callable[[Any, Any], float]
        A DSPy-compatible metric function.
    """

    def dspy_metric(example: t.Any, prediction: t.Any) -> float:
        ground_truth = getattr(example, metric_name, None)
        predicted = getattr(prediction, metric_name, None)

        if ground_truth is None or predicted is None:
            return 0.0

        loss_value = loss([predicted], [ground_truth])

        return -float(loss_value)

    return dspy_metric
