import logging

log = logging.getLogger()
log.setLevel(logging.INFO)

log.debug('This is a debug message')
log.info('This is an info message')
log.warning('This is a warning message')
log.error('This is an error message')
log.critical('This is a critical message')