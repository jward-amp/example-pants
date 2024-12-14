import logging

from common.logging import configure_logging
from project2.fizzbuzz import buzz, fizz

configure_logging(logging.INFO)
logger = logging.getLogger(__name__)

for n in range(1, 21):
    msg = f"{fizz(n)}{buzz(n)}"
    log = logger.info if msg else logger.debug
    log("n=%d: %s", n, msg or n)
