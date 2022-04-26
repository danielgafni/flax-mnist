from dataclasses import dataclass

from hydra.core.config_store import ConfigStore


@dataclass
class Config:
    """
    Hydra config schema. The values can be found at `conf/config.yaml`.
    """

    workdir: str
    learning_rate: float
    momentum: float
    batch_size: int
    num_epochs: int
    device: str


def store_config():
    cs = ConfigStore.instance()
    cs.store(name="base_config", node=Config)
