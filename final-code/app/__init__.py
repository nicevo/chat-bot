import os
from flask import Flask

application = Flask(__name__)

from app import views

if os.environ.get('HEROKU') is not None:
    import logging

    stream_handler = logging.StreamHandler()
    application.logger.addHandler(stream_handler)
    application.logger.setLevel(logging.DEBUG)
