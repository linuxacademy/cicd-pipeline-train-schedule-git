"""Environment configuration values used by lambda functions."""

import os

LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO')
SQS_MAIN_URL = os.getenv('SQS_MAIN_URL')
INTERVAL_SECONDS = int(os.getenv('INTERVAL_SECONDS'))
MAX_ATTEMPS = int(os.getenv('MAX_ATTEMPS'))
BACKOFF_RATE = int(os.getenv('BACKOFF_RATE'))
MESSAGE_RETENTION_PERIOD = int(os.getenv('MESSAGE_RETENTION_PERIOD'))
