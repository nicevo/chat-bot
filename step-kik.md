# Step 3: Basic Kik bot

We now need to tell Kik or Telegram that we want to develop a bot for their platform (a.k.a. their app), otherwise users will not be able to find out bot in the app.

## Tell Kik you want to create a bot

- **On phone:** Start Kik on your phone.

- **On computer:** Go to <https://dev.kik.com/>.

- **On phone:** Scan the Kik code with the Kik app.
- **On phone:** The user Botsworth will start chatting with you and ask you what the bot should be called.

- **On computer:** Click the Log in-button on Kik's web page and scan the Kik code with the app. Then go to the account Configuration (still on your computer) to find your new bot's API key (on <https://dev.kik.com/#/engine>). The API key is your bot's password.
- **On computer:** Save the API key in a text file, for later use.

We're now ready to start developing our Kik bot! Move on to the next step.

## Basic code
- [Download and extract code to a new folder](https://github.com/nicevo/helloworld-klarna/archive/step-kik.zip)
- Change to the folder and do the same commands from [Step 2](./step-heroku.md):
```
heroku apps:create
heroku builds:create --app NAME_OF_YOUR_HEROKU_APPLICATION
heroku ps:scale web=1 --app NAME_OF_YOUR_HEROKU_APPLICATION
heroku open --app NAME_OF_YOUR_HEROKU_APPLICATION
```
- Update the "callback address" to which Kik should send incoming messages `app/__init__.py`. Change the webhook parameter to match your Heroku app name (NAME_OF_YOUR_HEROKU_APPLICATION).
- Add [Kik bot username and API key](https://dev.kik.com/#/engine) in your app by entering these commands in your terminal:
```
heroku config:set KIK_BOT_USERNAME=your-bot-username --app NAME_OF_YOUR_HEROKU_APPLICATION 
heroku config:set KIK_BOT_APIKEY=your-bot-api-key --app NAME_OF_YOUR_HEROKU_APPLICATION
```
- Re-deploy to Heroku using the same command as before:
```
heroku builds:create --app NAME_OF_YOUR_HEROKU_APPLICATION
```
- Start chatting with your bot. You should now be able to find your bot in Kik by searching for it using the name you sent to Botsworth earlier. 
- Verify that it sends back everything you send to it.

This whole project is basically a copy of <https://kik.readthedocs.io/en/latest/user.html#example-bot>.

# No response from the bot? 
You can look at the logs using this command:

```
heroku logs -t --app NAME_OF_YOUR_HEROKU_APPLICATION
```
## A Closer Look

Want to know more about Kik bots? Check out <http://kik.readthedocs.io/en/latest/index.html>.

That is it, or maybe just the beginning!?

You now have a fully functional bot! 

## Next steps

In `app/views.py` there is a function called `process_text`. Use that to change the text and make the bot smarter.

If you want something to get you started you can try these [ideas on chat bots](./bots-ideas.md).`

[Back to index](./index.md)
