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
    j = json.loads(request.get_data())
    m = j['message']
    msg = Message.from_result(m)
    print 'Raw message:', msg

    try:
        print 'Received this message from user %d (%s): %s' % (msg.sender.id, msg.sender.first_name, msg.text)
        chat_id = msg.chat.id
        message = msg.text
        if message.lower() == '/start':
            response = on_start(chat_id)
        else:
            response = on_myname(chat_id, msg.text)
    except Exception as e:
        print "ERROR: ", e.message

    return Response(status=200)


def on_start(chat_id):
    print '/start received, chat_id=%i' % chat_id
    message = "Hi, what's your name?"
    return respond_with_message(chat_id, message)


def on_myname(chat_id, text):
    print 'Name received, chat_id=%i' % chat_id
    with application.app_context():
        player = db.session.query(models.Player).filter_by(name=text).first()
        if player is None:
            player = models.Player(name=text, visits=1)
            db.session.add(player)
            db.session.commit()
            respond_with_message(chat_id, "Welcome to your first chat " + player.name)
        else:
            player.visits += 1
            db.session.commit()
            respond_with_message(chat_id, "Nice to see you again " + player.name)

        respond_with_message(chat_id, "Let's learn some Geography!")
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
