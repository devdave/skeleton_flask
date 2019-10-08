
from flask import render_template
from logging import getLogger
from codex import app

log = getLogger(__name__)


@app.route("/", methods=["GET"])
def index():
    log.debug("Hello world")
    trail = [
        dict(href="/", name="Home")
    ]
    return render_template("page_basic.html", title="Hello World", trail=trail)