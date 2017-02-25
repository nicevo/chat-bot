# Let the app company know you exist
 
We now need to tell Kik or Telegram that we want to develop a bot for their platform (a.k.a. their app), otherwise users will not be able to find out bot in the app.
 
Tell Telegram you want to create a bot

1.  On phone: Start Telegram.
1.  On phone: Start chatting with the bot BotFather.
1.  On phone: Answer BotFather’s questions.
1.  On phone: After a couple of questions you will get a message starting with “Done! Congratulations…”. This message will contain your API key.
1.  On computer: Save the API key in a text file, for later use.

We’re now ready to start developing our Telegram bot! Move on to the next step.

Get the source code from https://github.com/mikaelsvensson/helloworld-klarna/archive/challenge-4-telegram.zip, or continue on your previous project.

The new stuff is in these files:
*   ```requirements.txt```
*   ```app/__init__.py```: Initialise the bot library with your own bot’s credentials.
*   ```app/views.py```: Defines functionality which takes care of the messages sent to our “callback address”. The sample code only returns what was sent, so it basically just verifies that the bot is alive.
*   ```init_webhook.py```: separate Python script used to tell Telegram about the address of our web service, i.e. the “callback address” to which Telegram should send incoming messages. Change the webhook parameter to match your Heroku app name.
*   ```Procfile```: Runs init_webhook.py and then starts the “chat bot webservice”.
*   ```ssl-certificate.herokuapp-com.pem```: https certificate used to encrypt the messages.

Make sure you have the correct dependencies (Python packages) installed. There are multiple packages 
available for creating Telegram bots in Python and in this session we will use one called twx.botapi.

Make sure you have this line in your requirements.txt:
    
    twx.botapi==3.1.1
 
Open init_webhook.py and make sure the URL of your application name matches what is in the set_webhook call.

Store your Telegram bot credentials (i.e. the API key sent to you by BotFather) in your Heroku application by entering this command in your terminal:
    
    heroku config:set TELEGRAM_BOT_APIKEY=your-bot-api-key

Add --app A_NAME_OF_YOUR_CHOICE at the end of the above command if you have multiple applications in your Heroku account.

Re-deploy to Heroku using the same command as before:
    
    heroku builds:create -a A_NAME_OF_YOUR_CHOICE
 
You should now be able to find your bot in Telegram by searching for it using the name you sent to 
BotFather earlier. Start chatting with it and verify that it sends back everything you send to it.
 
Want to know more about Telegram bots? Check out https://core.telegram.org/bots.

That is it, or maybe just the beginning!?

You now have a fully functional bot! It doesn’t do much yet but now it’s up to you to make it amazing!
