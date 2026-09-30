from isaivam.llms.base import (
    BaseRagasLLM,
    InstructorBaseRagasLLM,
    InstructorLLM,
    InstructorTypeVar,
    LangchainLLMWrapper as _LangchainLLMWrapper,
    LlamaIndexLLMWrapper as _LlamaIndexLLMWrapper,
    llm_factory,
)
from isaivam.llms.haystack_wrapper import HaystackLLMWrapper
from isaivam.llms.litellm_llm import LiteLLMStructuredLLM
from isaivam.llms.oci_genai_wrapper import OCIGenAIWrapper, oci_genai_factory
from isaivam.utils import DeprecationHelper

# Create deprecation wrappers for legacy classes
LangchainLLMWrapper = DeprecationHelper(
    _LangchainLLMWrapper,
    "LangchainLLMWrapper is deprecated and will be removed in a future version. "
    "Use llm_factory instead: "
    "from openai import OpenAI; "
    "from isaivam.llms import llm_factory; "
    "llm = llm_factory('gpt-4o-mini', client=OpenAI(api_key='...'))",
)

LlamaIndexLLMWrapper = DeprecationHelper(
    _LlamaIndexLLMWrapper,
    "LlamaIndexLLMWrapper is deprecated and will be removed in a future version. "
    "Use llm_factory instead: "
    "from openai import OpenAI; "
    "from isaivam.llms import llm_factory; "
    "llm = llm_factory('gpt-4o-mini', client=OpenAI(api_key='...'))",
)

__all__ = [
    "BaseRagasLLM",
    "HaystackLLMWrapper",
    "InstructorBaseRagasLLM",
    "InstructorLLM",
    "LangchainLLMWrapper",
    "LlamaIndexLLMWrapper",
    "LiteLLMStructuredLLM",
    "OCIGenAIWrapper",
    "InstructorTypeVar",
    "llm_factory",
    "oci_genai_factory",
]
