import logging


class base_class:
    def get_logger(self):
        logger = logging.getLogger(__name__)
        # what to print - log format
        formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
        # where to print - log location
        file_handler = logging.FileHandler('logfile.log')
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
        logger.setLevel(logging.CRITICAL)
        return logger