"""
pathなどの定数やaws/gcpクライアントのようなグローバルにひとつ存在すればよいstatelessな変数やインスタンスを配置
"""
import datetime
import json
import os
from pathlib import Path
from typing import Literal

from pydantic.dataclasses import dataclass
from pydantic.json import pydantic_encoder

from package.common.setup_logger import setup_logger
from package.module1.config import MD1Config

HOME: Path = Path(__file__).resolve().parents[1]
ROOT: Path = Path(__file__).resolve().parents[0]
CACHE_DIR: Path = ROOT / "__cache__"

CONFIG_FILENAME = os.environ.get("CONFIG_FILENAME", "config.json")


@dataclass
class Config:

    strategy: Literal["GP-EI", "TPE", "CMA-ES"]

    date_start: datetime.date

    MD1: MD1Config

    def __str__(self):
        return json.dumps(self, indent=4, default=pydantic_encoder, ensure_ascii=False)


def load_config():

    filepath = HOME / "config" / CONFIG_FILENAME

    with open(filepath, "r") as f:
        config_dict = json.loads(f.read())

    try:
        config = Config(**config_dict)
    except TypeError:
        print("====" * 15)
        print(f"Error: config/{CONFIG_FILENAME}とConfigデータクラスが不整合")
        print("====" * 15)
        raise

    return config


config = load_config()

logger = setup_logger()


def print(message: str, level: str = "info"):
    getattr(logger, level)(message)
