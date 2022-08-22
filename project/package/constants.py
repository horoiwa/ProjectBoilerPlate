"""
pathなどの定数やaws/gcpクライアントのようなグローバルにひとつ存在すればよいstatelessな変数やインスタンスを配置
"""
import datetime
import logging
from pathlib import Path
from typing import Literal
import json
import os

from pydantic.dataclasses import dataclass
from pydantic.json import pydantic_encoder

from package.module1.config import MD1Config


HOME: Path = Path(__file__).resolve().parents[1]
ROOT: Path = Path(__file__).resolve().parents[0]
CACHE_DIR: Path = ROOT / "__cache__"

TODAY: str = datetime.datetime.today().strftime("%Y%m%d")


@dataclass
class Config:

    strategy: Literal["GP-EI", "TPE", "CMA-ES"]

    date_start: datetime.date

    MD1: MD1Config

    def __str__(self):
        return json.dumps(self, indent=4, default=pydantic_encoder, ensure_ascii=False)


def _setup_config():

    config_filename = os.environ.get("CONFIG_FILENAME", "config.json")
    filepath = HOME / "config" / config_filename

    with open(filepath, "r") as f:
        config_dict = json.loads(f.read())

    try:
        config = Config(**config_dict)
    except TypeError:
        print("===="*15)
        print("Error: config.jsonとConfigデータクラスが不整合")
        print("===="*15)
        raise

    return config


config = _setup_config()


def _setup_logger():

    log_dir: Path = Path("/log") / TODAY
    if not log_dir.exists():
        log_dir.mkdir()

    logger = logging.getLogger("project")
    logger.setLevel(logging.DEBUG)

    formatter = logging.Formatter(
        '[%(levelname)s] %(asctime)s %(filename)s:%(lineno)d %(message)s',
        datefmt='%m/%d:%I:%M')

    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.INFO)
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)

    file_handler = logging.FileHandler(
        log_dir / "log.txt", mode='a', encoding='utf-8')
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    warning_handler = logging.FileHandler(
        log_dir / "warning.txt", mode='a', encoding='utf-8')
    warning_handler.setLevel(logging.WARN)
    warning_handler.setFormatter(formatter)
    logger.addHandler(warning_handler)

    return logger


logger = _setup_logger()


def print(message: str, level: str = "info"):
    getattr(logger, level)(message)
