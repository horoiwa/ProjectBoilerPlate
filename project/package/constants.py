"""
pathなどの定数やaws/gcpクライアントのようなグローバルにひとつ存在すればよいstatelessな変数やインスタンスを配置
"""
from pathlib import Path
import os

from pydantic import validator
from pydantic.dataclasses import dataclass

from package.module1.config import Module1Config


HOME: Path = Path(__file__).resolve().parents[1]

CONFIG_FILEPATH = os.environ.get("CONFIG_PATH", default=HOME / "config.yaml")


@dataclass
class ConfigSchema:

    LOG_DIR: Path

    project_name: str

    MODULE1: Module1Config


def load_config():
    pass


config = load_config()


def get_logger():
    return None

logger = get_logger()



if __name__ == '__main__':
    print("constatns")
    import pdb; pdb.set_trace()
