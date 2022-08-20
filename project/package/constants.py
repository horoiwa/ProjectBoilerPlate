"""
pathなどの定数やaws/gcpクライアントのようなグローバルにひとつ存在すればよいstatelessな変数やインスタンスを配置
"""
import datetime
import logging
from pathlib import Path
from typing import Union

from pydantic.dataclasses import dataclass

from package.module1.config import Module1Config
from package.config import PathConfig


HOME: Path = Path(__file__).resolve().parents[1]
ROOT: Path = Path(__file__).resolve().parents[0]

TODAY: str = datetime.datetime.today().strftime("%Y%m%d")


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


@dataclass
class RootConfig:

    PATH: PathConfig

    MODULE1: Module1Config



def _setup_config():
    pass


def reload_config(config_path: Union[str, Path]):
    pass


config = _setup_config()
