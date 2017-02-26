# Challenge 3: Let the app company know you exist

We now need to tell Kik or Telegram that we want to develop a bot for their platform (a.k.a. their app), 
otherwise users will not be able to find out bot in the app.

## Step By Step

1.  Tell Kik you want to create a bot
    1.  On phone: Start Kik on your phone.
    1.  On computer: Go to https://dev.kik.com/ on your computer.
    1.  On phone: Scan the Kik code with the Kik app.
    1.  On phone: The user Botsworth will start chatting with you and ask you what the bot should be called.
    1.  On computer: Click the Log in-button on Kik’s web page and scan the Kik code with the app. 
        Then go to the account Configuration (still on your computer) to find your new bot’s API key 
        (on https://dev.kik.com/#/engine). The API key is your bot's password.
    1.  On computer: Save the API key in a text file, for later use.
    1.  We’re now ready to start developing our Kik bot! Move on to the next step.

1.  If you have _not completed Challenge 2_ and just want to do Challenge 3 right away:

    1.  Do the "Get started with Heroku" steps from [Challenge 2](./challenge-heroku.md).
        
    1.  Download and extract https://github.com/mikaelsvensson/helloworld-klarna/archive/challenge-4-kik.zip 
        to a new folder, for example ```helloworld-klarna```.

1.  If you have _already completed Challenge 2_ and just want to continue on that project:

    1.  Go to https://github.com/mikaelsvensson/helloworld-klarna/tree/challenge-4-kik and find "inspiration"
        for the next couple of steps. Copy and paste as much code as you think is needed.

    1.  Update ```requirements.txt```: Kik bot library added. We will be using the official Python package for Kik bots. 
        Make sure you have this line in your requirements.txt: ```kik==1.2.0```
    
    1.  Update ```app/__init__.py```: Initialise the bot library with your own bot’s credentials and the 
        address of our web service, i.e. the “callback address” to which Kik should send incoming messages. 
        Change the webhook parameter to match your Heroku app name.
    
    1.  Update ```app/views.py```: Defines functionality which takes care of the messages sent to our “callback address”.

1.  Store your Kik bot credentials (bot username and API key found on https://dev.kik.com/#/engine) in your 
    Heroku application by entering these commands in your terminal:
    
        heroku config:set KIK_BOT_USERNAME=your-bot-username --app NAME_OF_YOUR_HEROKU_APPLICATION
        heroku config:set KIK_BOT_APIKEY=your-bot-api-key --app NAME_OF_YOUR_HEROKU_APPLICATION
 
1.  Re-deploy to Heroku using the same command as before:

        heroku builds:create --app NAME_OF_YOUR_HEROKU_APPLICATION
 
You should now be able to find your bot in Kik by searching for it using the name you sent to Botsworth 
earlier. Start chatting with it and verify that it sends back everything you send to it.

The sample code only returns what was sent, so it basically just verifies that the bot is alive. This whole 
project is basically a copy of https://kik.readthedocs.io/en/latest/user.html#example-bot.

No response from the bot? You can look at the logs using this command:

    heroku logs -t --app NAME_OF_YOUR_HEROKU_APPLICATION