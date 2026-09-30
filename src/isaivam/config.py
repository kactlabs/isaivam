from __future__ import annotations

import typing as t

from pydantic import BaseModel, Field, field_validator

from isaivam.embeddings.base import BaseIsaivamEmbeddings
from isaivam.llms.base import BaseIsaivamLLM
from isaivam.losses import Loss
from isaivam.optimizers import GeneticOptimizer, Optimizer

DEFAULT_OPTIMIZER_CONFIG = {"max_steps": 100}


class DemonstrationConfig(BaseModel):
    embedding: t.Any  # this has to be of type Any because BaseIsaivamEmbedding is an ABC
    enabled: bool = True
    top_k: int = 3
    threshold: float = 0.7
    technique: t.Literal["random", "similarity"] = "similarity"

    @field_validator("embedding")
    def validate_embedding(cls, v):
        if not isinstance(v, BaseIsaivamEmbeddings):
            raise ValueError("embedding must be an instance of BaseIsaivamEmbeddings")
        return v


class InstructionConfig(BaseModel):
    llm: BaseIsaivamLLM
    enabled: bool = True
    loss: t.Optional[Loss] = None
    optimizer: Optimizer = GeneticOptimizer()
    optimizer_config: t.Dict[str, t.Any] = Field(
        default_factory=lambda: DEFAULT_OPTIMIZER_CONFIG
    )
