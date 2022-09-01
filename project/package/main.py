from package.constants import config, logger, print
from package.sub import sub


def main(msg: str):
    print("Hello!")
    logger.debug(f"Hello, {msg}")
    logger.info(f"Hello, {msg}")
    logger.warn(f"Hello, {msg}")
    logger.error(f"Hello, {msg}")
    logger.critical(f"Criticl, {msg}")
    print(config)
    print("hello")
    print("hello", level="critical")
    sub()


if __name__ == "__main__":
    main(msg="spam")
