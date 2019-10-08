
from .. import app
import sys
import logging



class BaseConfig(object):
    APP_LOGGING_HANDLER = logging.NullHandler()
    APP_LOGGING_FMT = "|%(levelname)s|[%(name)s:%(lineno)s] %(message)s"
    APP_LOGGING_LEVEL = logging.ERROR


class DevConfig(BaseConfig):
    APP_LOGGING_HANDLER = logging.StreamHandler(stream=sys.stderr)
    APP_LOGGING_LEVEL = logging.DEBUG
    RUN_PORT=8080
    DEBUG = True


class ProdConfig(BaseConfig):
    RUN_PORT=8000


class TestConfig(BaseConfig):
    RUN_PORT=5050


# Use flask's logger this one time before it is replaced by our own
app.logger.debug(f"conf/__init__.py - Loading {app.env}")
if app.env == "development":
    app.config.from_object(DevConfig)
else:
    app.config.from_object(ProdConfig)