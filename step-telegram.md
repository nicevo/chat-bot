# Step 3: Basic Telegram bot

We now need to tell Kik or Telegram that we want to develop a bot for their platform (a.k.a. their app), otherwise users will not be able to find out bot in the app.

## Step By Step

### Tell Telegram you want to create a bot

- **On phone:** Start Telegram.
- **On phone:** Start chatting with the bot BotFather.
- **On phone:** Answer BotFather's questions.
- **On phone:** After a couple of questions you will get a message starting with "Done! Congratulations...". This message will contain your API key (i.e. the password for your bot).

- **On computer:** Save the API key in a text file, for later use.

We're now ready to start developing our Telegram bot! Move on to the next step.


- [Download and extract code to a new folder](https://github.com/nicevo/helloworld-klarna/archive/step-telegram.zip)
- Change to the folder and do the same commands from [Step 2](./step-heroku.md):
```
heroku apps:create
```
- Open `init_webhook.py` and make sure the URL of your application name matches what is in the `set_webhook` call.
- Store your Telegram bot credentials (i.e. the API key sent to you by BotFather) in your Heroku application by entering this command in your terminal:
```
heroku config:set TELEGRAM_BOT_APIKEY=your-bot-api-key --app NAME_OF_YOUR_HEROKU_APPLICATION
```
- Re-deploy to Heroku using the same command as before:
```
heroku builds:create --app NAME_OF_YOUR_HEROKU_APPLICATION
heroku ps:scale web=1 --app NAME_OF_YOUR_HEROKU_APPLICATION
heroku open --app NAME_OF_YOUR_HEROKU_APPLICATION
```
- Start chatting with your bot. You should now be able to find your bot in Telegram by searching for it using the name you sent to BotFather earlier. 
- Verify that it sends back everything you send to it.

## A Closer Look

Want to know more about Telegram bots? Check out <https://core.telegram.org/bots>.

That is it, or maybe just the beginning!?

You now have a fully functional bot!

## Next steps

In `app/views.py` there is a function called `process_text`. Use that to change the text and make the bot smarter.

If you want something to get you started you can try these [ideas on chat bots](./bots-ideas.md).`

[Back to index](./index.md)
