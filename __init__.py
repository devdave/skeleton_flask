
import logging
import sys
from flask import Flask

app:Flask = Flask(__name__)
log:logging.Logger = None

def create_app(config=None)->Flask:
    global app, log


    from . import conf

    log = logging.getLogger(__name__)
    fmt = logging.Formatter(app.config['APP_LOGGING_FMT'])
    hndl = app.config['APP_LOGGING_HANDLER']  # type: logging.Handler
    hndl.setFormatter(fmt)
    hndl.setLevel(app.config["APP_LOGGING_LEVEL"])
    log.propagate = False
    log.handlers.clear() # This removes flask's default handler
    log.addHandler(hndl)
    log.debug(f"{__name__} loading components")



    from . import lib
    from . import models
    from . import views
    from . import settings

    return app


