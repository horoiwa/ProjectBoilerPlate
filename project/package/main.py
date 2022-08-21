from package.constants import config, logger, print
from package.sub import sub


def main(msg: str):
    print("Hello!")
    logger.info(f"Hello, {msg}")
    logger.critical(f"Criticl, {msg}")

    print(config)

    sub()


if __name__ == '__main__':
    main(msg="spam")
