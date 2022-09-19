"""
pathなどの定数やaws/gcpクライアントのようなグローバルにひとつ存在すればよいstatelessな変数やインスタンスを配置
"""
import copy
import datetime
import json
import logging
import os
import sys
from pathlib import Path
from typing import Literal

from pydantic.dataclasses import dataclass
from pydantic.json import pydantic_encoder

from package.module1.config import MD1Config

HOME: Path = Path(__file__).resolve().parents[1]
ROOT: Path = Path(__file__).resolve().parents[0]
CACHE_DIR: Path = ROOT / "__cache__"

CONFIG_FILENAME = os.environ.get("CONFIG_FILENAME", "config.json")

TODAY: str = datetime.datetime.today().strftime("%Y%m%d")


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


class ColoredStreamHandler(logging.StreamHandler):

    # From https://pod.hatenablog.com/entry/2020/03/01/221715
    cmap = {
        "TRACE": "[TRACE]",
        "DEBUG": "\x1b[0;36mDEBUG\x1b[0m",
        "INFO": "\x1b[0;32mINFO\x1b[0m",
        "WARNING": "\x1b[0;33mWARN\x1b[0m",
        "WARN": "\x1b[0;33mwWARN\x1b[0m",
        "ERROR": "\x1b[0;31mERROR\x1b[0m",
        "ALERT": "\x1b[0;37;41mALERT\x1b[0m",
        "CRITICAL": "\x1b[0;37;41mCRITICAL\x1b[0m",
    }

    def emit(self, record: logging.LogRecord) -> None:
        record = copy.deepcopy(record)
        record.levelname = self.cmap[record.levelname]
        super().emit(record)


def _setupLogger():

    log_dir: Path = HOME / "log" / TODAY
    if not log_dir.exists():
        log_dir.mkdir(parents=True)

    logger_name = "project"
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.DEBUG)

    formatter = logging.Formatter(
        "[%(levelname)s] %(asctime)s %(filename)s:%(lineno)d %(message)s",
        datefmt="%m/%d:%I:%M",
    )

    stream_handler = ColoredStreamHandler(stream=sys.stdout)
    stream_handler.setLevel(logging.INFO)
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)

    file_handler = logging.FileHandler(log_dir / "all.log", mode="a", encoding="utf-8")
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    warning_handler = logging.FileHandler(log_dir / "warnings.log", mode="a", encoding="utf-8")
    warning_handler.setLevel(logging.WARN)
    warning_handler.setFormatter(formatter)
    logger.addHandler(warning_handler)

    return logger


logger = _setupLogger()


def getChildLogger(name):
    child_logger = logger.getChild(name)
    return child_logger


def print(message: str, level: str = "info"):
    getattr(logger, level)(message)
