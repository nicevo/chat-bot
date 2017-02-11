import time
from flask import render_template, request, Response
from kik.messages import messages_from_json, TextMessage

from app import application
from app import kik


@application.route('/')
def index():
    return "Hej"


@application.route('/time')
def show_time():
    return render_template(
        'time.html',
        now=time.strftime("%c")
    )


@application.route('/callback/kik', methods=['POST'])
def incoming():
    if not kik.verify_signature(request.headers.get('X-Kik-Signature'), request.get_data()):
        return Response(status=403)

    messages = messages_from_json(request.json['messages'])

    for message in messages:
        if isinstance(message, TextMessage):
            kik.send_messages([
                TextMessage(
                    to=message.from_user,
                    chat_id=message.chat_id,
                    body=message.body
                )
            ])

    return Response(status=200)
