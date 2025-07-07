import logging
import sys

logging.basicConfig(
    handlers=[logging.StreamHandler(sys.stdout)],
    format='%(asctime)s %(levelname)s %(name)s: %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    level=logging.INFO
)

def get_logger(name):
    return logging.getLogger(name)