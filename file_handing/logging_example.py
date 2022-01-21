import logging

# logging level
# DEBUG > INFO > WARNING > ERROR > Critical

# logging.debug("틀렸어!")
# logging.info("확인해!")
# logging.warning("조심해!")
# logging.error("에러났어!")
# logging.critical("망했어!")


# logging level setting
if __name__ == '__main__':
    logger = logging.getLogger("main")
    logging.basicConfig(level=logging.DEBUG)
    logger.setLevel(logging.INFO)

    steam_handler = logging.FileHandler(
        "file_handling/log/my.log", mode="w", encoding="utf8")
    logger.addHandler(steam_handler)

    logger.debug("틀렸어!")
    logger.info("확인해!")
    logger.warning("조심해!")
    logger.error("에러났어!")
    logger.critical("망했어!")