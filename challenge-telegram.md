# Challenge 3: Let the app company know you exist
 
We now need to tell Kik or Telegram that we want to develop a bot for their platform (a.k.a. their app), otherwise users will not be able to find out bot in the app.
 
1.  Tell Telegram you want to create a bot

    1.  On phone: Start Telegram.
    1.  On phone: Start chatting with the bot BotFather.
    1.  On phone: Answer BotFather’s questions.
    1.  On phone: After a couple of questions you will get a message starting with “Done! Congratulations…”. This message will contain your API key.
    1.  On computer: Save the API key in a text file, for later use.
    1.  We’re now ready to start developing our Telegram bot! Move on to the next step.

1.  If you have _not completed Challenge 2_ and just want to do Challenge 3 right away:

    1.  Do the "Get started with Heroku" steps from [Challenge 2](./challenge-heroku.md).
    
    1.  Download and extract https://github.com/mikaelsvensson/helloworld-klarna/archive/challenge-4-telegram.zip 
        to a new folder, for example ```helloworld-klarna```.

1.  If you have _already completed Challenge 2_ and just want to continue on that project:

    1.  Go to https://github.com/mikaelsvensson/helloworld-klarna/tree/challenge-4-telegram and find "inspiration"
        for the next couple of steps. Copy and paste as much code as you think is needed.

    1.  Update ```app/__init__.py```: Initialise the bot library with your own bot’s credentials.
    
    1.  Update ```app/views.py```: Defines functionality which takes care of the messages sent to our “callback address”. The sample code only returns what was sent, so it basically just verifies that the bot is alive.
    
    1.  Add ```init_webhook.py```: separate Python script used to tell Telegram about the address of our web service, i.e. the “callback address” to which Telegram should send incoming messages. Change the webhook parameter to match your Heroku app name.
    
    1.  Update ```Procfile```: Runs init_webhook.py and then starts the “chat bot webservice”.
    
    1.  Add ```ssl-certificate.herokuapp-com.pem```: https certificate used to encrypt the messages.

1.  Make sure you have the correct dependencies (Python packages) installed. There are multiple packages 
    available for creating Telegram bots in Python and in this session we will use one called twx.botapi.

    Make sure you have this line in your requirements.txt:
    
        twx.botapi==3.1.1
 
1.  Open init_webhook.py and make sure the URL of your application name matches what is in the set_webhook call.

1.  Store your Telegram bot credentials (i.e. the API key sent to you by BotFather) in your Heroku application by entering this command in your terminal:
    
        heroku config:set TELEGRAM_BOT_APIKEY=your-bot-api-key --app NAME_OF_YOUR_HEROKU_APPLICATION

1.  Re-deploy to Heroku using the same command as before:
    
        heroku builds:create --app NAME_OF_YOUR_HEROKU_APPLICATION
 
You should now be able to find your bot in Telegram by searching for it using the name you sent to 
BotFather earlier. Start chatting with it and verify that it sends back everything you send to it.

## A Closer Look

Want to know more about Telegram bots? Check out https://core.telegram.org/bots.

That is it, or maybe just the beginning!?

You now have a fully functional bot! It doesn’t do much yet but now it’s up to you to make it amazing!
