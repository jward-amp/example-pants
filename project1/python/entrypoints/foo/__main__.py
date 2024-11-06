import logging

from common.logging import configure_logging
from project1.foo import foo

configure_logging(logging.INFO)
logger = logging.getLogger(__name__)
logger.debug("starting foo ...")
logger.info(foo())
logger.debug("finished foo.")
