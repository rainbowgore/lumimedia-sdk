import logging

logger = logging.getLogger("lumimedia")
logger.setLevel(logging.DEBUG)

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)

formatter = logging.Formatter('[%(levelname)s] %(asctime)s - %(message)s')
console_handler.setFormatter(formatter)

logger.addHandler(console_handler)

def log_info(message):
    logger.info(message)

def log_warning(message):
    logger.warning(message)

def log_error(message):
    logger.error(message)

def log_debug(message):
    logger.debug(message)