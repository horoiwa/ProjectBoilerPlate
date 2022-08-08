from pathlib import Path

"""
PATHなどの定数やAWS/GCPクライアントのようなグローバルにひとつ存在すればよいインスタンスを配置
"""

HOME = Path(__file__).resolve().parents[1]
ROOT = Path(__file__).resolve().parents[0]
