from pathlib import Path

from package.common.logging import get_logger
from package.config import load_config
"""
PATHなどの定数やAWS/GCPクライアントのようなグローバルにひとつ存在すればよいstatelessな変数やインスタンスを配置
"""

HOME = Path(__file__).resolve().parents[1]
ROOT = Path(__file__).resolve().parents[0]

logger = get_logger()

config = load_config()
