from loguru import logger

logger.add("logs/ai.log", rotation="1 MB")

logger.info("Logger initialized")
