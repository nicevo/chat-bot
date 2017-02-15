import os

from flask import Flask
from kik import KikApi, Configuration

application = Flask(__name__)

bot_username = os.environ.get('KIK_BOT_USERNAME')
bot_api_key = os.environ.get('KIK_BOT_APIKEY')

kik = KikApi(bot_username, bot_api_key)

kik.set_configuration(Configuration(
    webhook='https://A_NAME_OF_YOUR_CHOICE.herokuapp.com/callback/kik'))

from app import views

if os.environ.get('HEROKU') is not None:
    import logging

    stream_handler = logging.StreamHandler()
    application.logger.addHandler(stream_handler)
    application.logger.setLevel(logging.DEBUG)
