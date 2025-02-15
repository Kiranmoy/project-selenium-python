import logging

# LOG LEVELS: DEBUG | INFO |WARNING | ERROR | CRITICAL
# FORMAT: <date> <timestamp> : LEVEL : <test-case-name> : <log-message>

# Logger
logger = logging.getLogger(__name__)

# what to print - log format
formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")

# where to print - log location
fileHandler = logging.FileHandler('logfile.log')
fileHandler.setFormatter(formatter)
logger.addHandler(fileHandler)

logger.setLevel(logging.DEBUG)

logger.debug("debug statement")
logger.info("info statement")
logger.warning("warning statement")
logger.error("error statement")
logger.critical("critical statement")

logging.basicConfig(
    format="%(asctime)s : %(levelname)s : %(name)s : %(message)s",
    style="{",
    datefmt="%Y-%m-%d %H:%M",
)