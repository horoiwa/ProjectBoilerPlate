from package.constants import config, logger, print


def main(msg: str):
    print("Hello!")
    logger.info(f"Hello, {msg}")
    logger.critical(f"Criticl, {msg}")

    print(config)


if __name__ == '__main__':
    main(msg="spam")
