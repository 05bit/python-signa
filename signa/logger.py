import os

__all__ = ('get_logger',)

LOGGER = None

USE_LOGURU = os.environ.get('LOGURU_DISABLED', '') not in ('true', '1')

try:
    if USE_LOGURU:
        import loguru
        LOGGER = loguru.logger
except ImportError:
    pass

if not LOGGER:
    import logging


def get_logger(*args):
    if LOGGER:
        return LOGGER
    return logging.getLogger(*args)
