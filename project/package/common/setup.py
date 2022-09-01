import logging
from pathlib import Path
import datetime


TODAY: str = datetime.datetime.today().strftime("%Y%m%d")


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


class ColoredStreamHandler(logging.StreamHandler):
    def emit(self, record: logging.LogRecord) -> None:
        record.levelname = cmap[record.levelname]
        super().emit(record)


def setup_logger():

    log_dir: Path = Path("/log") / TODAY
    if not log_dir.exists():
        log_dir.mkdir()

    logger = logging.getLogger("project")
    logger.setLevel(logging.DEBUG)

    formatter = logging.Formatter(
        "[%(levelname)s] %(asctime)s %(filename)s:%(lineno)d %(message)s",
        datefmt="%m/%d:%I:%M",
    )

    stream_handler = ColoredStreamHandler()
    stream_handler.setLevel(logging.INFO)
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)

    file_handler = logging.FileHandler(log_dir / "log.txt", mode="a", encoding="utf-8")
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    warning_handler = logging.FileHandler(log_dir / "warning.txt", mode="a", encoding="utf-8")
    warning_handler.setLevel(logging.WARN)
    warning_handler.setFormatter(formatter)
    logger.addHandler(warning_handler)

    return logger
