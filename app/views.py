import time
from flask import render_template, request, Response
from kik.messages import messages_from_json, TextMessage

from app import application
from app import kik


def process_text(message):
    incomming_text = message.body
    # Your code goes here
    my_response = incomming_text
    return my_response


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
            my_response = process_text(message)
            kik.send_messages([
                TextMessage(
                    to=message.from_user,
                    chat_id=message.chat_id,
                    body=my_response
                )
            ])

    return Response(status=200)
