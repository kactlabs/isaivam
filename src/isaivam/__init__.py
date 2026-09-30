from isaivam import backends
from isaivam.cache import CacheInterface, DiskCacheBackend, cacher
from isaivam.dataset import Dataset, DataTable
from isaivam.dataset_schema import EvaluationDataset, MultiTurnSample, SingleTurnSample
from isaivam.evaluation import aevaluate, evaluate
from isaivam.experiment import Experiment, experiment, version_experiment
from isaivam.run_config import RunConfig
from isaivam.tokenizers import (
    BaseTokenizer,
    HuggingFaceTokenizer,
    TiktokenWrapper,
    get_tokenizer,
)

try:
    from ._version import version as __version__
except ImportError:
    __version__ = "unknown version"


__all__ = [
    "evaluate",
    "aevaluate",
    "RunConfig",
    "__version__",
    "SingleTurnSample",
    "MultiTurnSample",
    "EvaluationDataset",
    "DataTable",
    "Dataset",
    "cacher",
    "CacheInterface",
    "DiskCacheBackend",
    "backends",
    "Experiment",
    "experiment",
    "version_experiment",
    "BaseTokenizer",
    "TiktokenWrapper",
    "HuggingFaceTokenizer",
    "get_tokenizer",
]


def __getattr__(name):
    if name == "experimental":
        try:
            import ragas_experimental as experimental  # type: ignore

            return experimental
        except ImportError:
            raise ImportError(
                "isaivam.experimental requires installation: "
                "pip install isaivam[experimental]"
            )
    raise AttributeError(f"module 'isaivam' has no attribute '{name}'")
