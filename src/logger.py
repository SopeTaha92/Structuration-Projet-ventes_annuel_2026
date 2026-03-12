


from loguru import logger


def logging_file(file):
    logger.remove()
    logger.add(
                file, 
                rotation="10 MB",
                retention="30 days",
                compression="zip",
                level="INFO",
                format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {name}:{line} | {message}"
                )
    