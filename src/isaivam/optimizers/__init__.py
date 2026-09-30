from isaivam.optimizers.base import Optimizer
from isaivam.optimizers.genetic import GeneticOptimizer

try:
    from isaivam.optimizers.dspy_optimizer import DSPyOptimizer

    __all__ = [
        "Optimizer",
        "GeneticOptimizer",
        "DSPyOptimizer",
    ]
except ImportError:
    __all__ = [
        "Optimizer",
        "GeneticOptimizer",
    ]
