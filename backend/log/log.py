import os
from logging import config, getLogger

if "LOGGING_CONF_PATH" in os.environ.keys():
    config.fileConfig(os.environ["LOGGING_CONF_PATH"])
    print(f"config_path={os.environ['LOGGING_CONF_PATH']}")
logger = getLogger(__name__)
