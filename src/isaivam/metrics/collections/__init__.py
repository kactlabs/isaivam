"""Collections of metrics using modern component architecture."""

from isaivam.metrics.collections._bleu_score import BleuScore
from isaivam.metrics.collections._rouge_score import RougeScore
from isaivam.metrics.collections._semantic_similarity import SemanticSimilarity
from isaivam.metrics.collections._string import (
    DistanceMeasure,
    ExactMatch,
    NonLLMStringSimilarity,
    StringPresence,
)
from isaivam.metrics.collections.agent_goal_accuracy import (
    AgentGoalAccuracy,
    AgentGoalAccuracyWithoutReference,
    AgentGoalAccuracyWithReference,
)
from isaivam.metrics.collections.answer_accuracy import AnswerAccuracy
from isaivam.metrics.collections.answer_correctness import AnswerCorrectness
from isaivam.metrics.collections.answer_relevancy import AnswerRelevancy
from isaivam.metrics.collections.base import BaseMetric
from isaivam.metrics.collections.chrf_score import CHRFScore
from isaivam.metrics.collections.context_entity_recall import ContextEntityRecall
from isaivam.metrics.collections.context_precision import (
    ContextPrecision,
    ContextPrecisionWithoutReference,
    ContextPrecisionWithReference,
    ContextUtilization,
)
from isaivam.metrics.collections.context_recall import ContextRecall
from isaivam.metrics.collections.context_relevance import ContextRelevance
from isaivam.metrics.collections.datacompy_score import DataCompyScore
from isaivam.metrics.collections.domain_specific_rubrics import (
    DomainSpecificRubrics,
    RubricsScoreWithoutReference,
    RubricsScoreWithReference,
)
from isaivam.metrics.collections.factual_correctness import FactualCorrectness
from isaivam.metrics.collections.faithfulness import Faithfulness
from isaivam.metrics.collections.instance_specific_rubrics import InstanceSpecificRubrics
from isaivam.metrics.collections.multi_modal_faithfulness import MultiModalFaithfulness
from isaivam.metrics.collections.multi_modal_relevance import MultiModalRelevance
from isaivam.metrics.collections.noise_sensitivity import NoiseSensitivity
from isaivam.metrics.collections.quoted_spans import QuotedSpansAlignment
from isaivam.metrics.collections.response_groundedness import ResponseGroundedness
from isaivam.metrics.collections.sql_semantic_equivalence import SQLSemanticEquivalence
from isaivam.metrics.collections.summary_score import SummaryScore
from isaivam.metrics.collections.tool_call_accuracy import ToolCallAccuracy
from isaivam.metrics.collections.tool_call_f1 import ToolCallF1
from isaivam.metrics.collections.topic_adherence import TopicAdherence

__all__ = [
    "BaseMetric",  # Base class
    # RAG metrics
    "AnswerAccuracy",
    "AnswerCorrectness",
    "AnswerRelevancy",
    "BleuScore",
    "CHRFScore",
    "ContextEntityRecall",
    "ContextRecall",
    "ContextPrecision",
    "ContextPrecisionWithReference",
    "ContextPrecisionWithoutReference",
    "ContextRelevance",
    "ContextUtilization",
    "DistanceMeasure",
    "ExactMatch",
    "FactualCorrectness",
    "Faithfulness",
    "MultiModalFaithfulness",
    "MultiModalRelevance",
    "NoiseSensitivity",
    "NonLLMStringSimilarity",
    "QuotedSpansAlignment",
    "ResponseGroundedness",
    "RougeScore",
    "SemanticSimilarity",
    "StringPresence",
    "SummaryScore",
    # Agent & Tool metrics
    "AgentGoalAccuracy",
    "AgentGoalAccuracyWithReference",
    "AgentGoalAccuracyWithoutReference",
    "ToolCallAccuracy",
    "ToolCallF1",
    "TopicAdherence",
    # Rubric metrics
    "DomainSpecificRubrics",
    "InstanceSpecificRubrics",
    "RubricsScoreWithoutReference",
    "RubricsScoreWithReference",
    # SQL & Data metrics
    "DataCompyScore",
    "SQLSemanticEquivalence",
]
