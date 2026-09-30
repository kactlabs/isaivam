# isaivam

*Supercharge your LLM application evaluations.*

`isaivam` is an evaluation framework for RAG and LLM applications. The name **isaivam** means *music* — a nod to its roots in "ragas". It provides objective metrics, test data generation, and data-driven insights so you can move away from slow, subjective assessments toward efficient, repeatable evaluation workflows.

## Key Features

- Objective metrics: Evaluate LLM applications using both LLM-based and traditional metrics.
- Test data generation: Automatically create comprehensive test datasets covering a wide range of scenarios.
- Integrations: Works with popular LLM frameworks like LangChain and major observability tools.
- Feedback loops: Leverage production data to continually improve your LLM applications.

## Installation

From source (editable):

```bash
pip install -e .
```

Dependencies are tracked in `requirements.txt`:

```bash
pip install -r requirements.txt
```

## Quickstart

`isaivam` comes with pre-built metrics for common evaluation tasks. For example, `DiscreteMetric` evaluates any aspect of your output:

```python
import asyncio
from openai import AsyncOpenAI
from isaivam.metrics import DiscreteMetric
from isaivam.llms import llm_factory

# Setup your LLM
client = AsyncOpenAI()
llm = llm_factory("gpt-4o", client=client)

# Create a custom aspect evaluator
metric = DiscreteMetric(
    name="summary_accuracy",
    allowed_values=["accurate", "inaccurate"],
    prompt="""Evaluate if the summary is accurate and captures key information.

Response: {response}

Answer with only 'accurate' or 'inaccurate'."""
)

# Score your application's output
async def main():
    score = await metric.ascore(
        llm=llm,
        response="The summary of the text is..."
    )
    print(f"Score: {score.value}")   # 'accurate' or 'inaccurate'
    print(f"Reason: {score.reason}")


if __name__ == "__main__":
    asyncio.run(main())
```

> Note: Make sure your `OPENAI_API_KEY` environment variable is set.

## CLI

The library installs an `isaivam` command for running experiments and evaluations:

```bash
isaivam evals <eval_file> --dataset <name> --metrics <fields>
```

## Analytics

`isaivam` collects minimal, anonymized usage data to guide development. To opt out, set the `ISAIVAM_DO_NOT_TRACK` environment variable to `true`.

## Acknowledgements

`isaivam` is derived from the open-source [ragas](https://github.com/vibrantlabsai/ragas) project (Apache-2.0). See `LICENSE` for details.
