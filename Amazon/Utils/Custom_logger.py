import logging
import os
from datetime import datetime

class LogGen:
    @staticmethod
    def init_logger(test_filename: str):
        log_dir = os.path.join(os.path.dirname(__file__), '..', 'Logs')
        os.makedirs(log_dir, exist_ok=True)

        base_name = os.path.splitext(os.path.basename(test_filename))[0]
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        log_file = os.path.join(log_dir, f"{base_name}_{timestamp}.log")

        logger = logging.getLogger(base_name)
        logger.setLevel(logging.DEBUG)

        if not logger.handlers:
            fh = logging.FileHandler(log_file, mode='w', delay=False)
            fh.setLevel(logging.DEBUG)
            fh.flush = lambda: fh.stream.flush()

            ch = logging.StreamHandler()
            ch.setLevel(logging.INFO)

            formatter = logging.Formatter(
                '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                datefmt='%Y-%m-%d %H:%M:%S'
            )

            fh.setFormatter(formatter)
            ch.setFormatter(formatter)

            logger.addHandler(fh)
            logger.addHandler(ch)

        return logger
