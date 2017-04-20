import time
import json
import random

from flask import render_template, request, Response
from twx.botapi import Message

from app import application
from app import bot
from app import models
from app import db


@application.route('/')
def index():
    return "Hej"


@application.route('/time')
def show_time():
    return render_template(
        'time.html',
        now=time.strftime("%c")
    )


@application.route('/incoming', methods=['POST'])
def incoming():
    requst_json = json.loads(request.get_data())
    message = Message.from_result(requst_json['message'])
    print 'Raw message:', message
    try:
        on_message(message)
    except Exception as e:
        print "ERROR: ", e.message

    return Response(status=200)


def on_message(message):
    print 'Received this message from user %d (%s): %s' % (message.sender.id, message.sender.first_name, message.text)
    chat_id = message.chat.id
    register_player(chat_id, message.sender)
    response = geography_quizz(chat_id)
    return response


def register_player(chat_id, sender):
    print 'Figuring out player name, chat_id=%i' % chat_id
    name = sender.first_name
    with application.app_context():
        player = db.session.query(models.Player).filter_by(name=name).first()
        if player is None:
            player = models.Player(name=name, visits=1)
            db.session.add(player)
            db.session.commit()
            respond_with_message(chat_id, "Welcome %s! It's great to finally meet you." % player.name)
        else:
            player.visits += 1
            db.session.commit()
            respond_with_message(chat_id, "Nice to see you again %s. This is your %ith visit" % (player.name, player.visits))


def geography_quizz(chat_id):
    respond_with_message(chat_id, "Let's learn some Geography!")
    with application.app_context():
        capitals = db.session.query(models.Capital).all()
        capital = random.choice(capitals)
        return respond_with_message(chat_id, "The captial of %s is %s" % (capital.country, capital.name))


def respond_with_message(chat_id, message):
    response = bot.send_message(
        chat_id=chat_id,
        text=message,
        parse_mode=None,
        disable_web_page_preview=None,
        reply_to_message_id=None,
        reply_markup=None,
        disable_notification=False).wait()
    return response
