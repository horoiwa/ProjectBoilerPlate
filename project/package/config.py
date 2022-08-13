from typing import List
from pathlib import Path

from pydantic.dataclasses import dataclass


CONFIG_CLASSES = {}

def register_config(config_cls):
    class_name = config_cls.__cls__.__name__
    if class_name not in CONFIG_CLASSES:
        CONFIG_CLASSES[class_name] = config_cls
    return config_cls


def load_config():
    return None


@register_config
@dataclass
class GeneralConfig:

    first_name: str
    last_name: str
    allowed_hosts: List[str]
    logdir: Path

    def __post_init__(self):
        """validationなど
        """
        assert len(self.project_name) < 30

    @property
    def full_name(self):
        return f"{self.last_name} {self.first_name}"
