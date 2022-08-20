from pathlib import Path

from pydantic.dataclasses import dataclass


@dataclass
class PathConfig:

    DATA_DIR: Path
    SAVE_DIR: Path
