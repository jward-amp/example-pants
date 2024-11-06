import logging

from common.logging import configure_logging
from project1.bar import bar

configure_logging(logging.DEBUG)
logger = logging.getLogger(__name__)
logger.debug("starting bar ...")
logger.info(bar())
logger.debug("finished bar.")
