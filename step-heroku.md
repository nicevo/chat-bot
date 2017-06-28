# Step 2: Publish to Heroku

In order to make our fancy web service (which still only tells the time of the day) available to everyone in the entire world to enjoy we will use the hosting service Heroku. The free service is more than enough for our needs.

## Getting started with Heroku

Heroku is the cloud platform we will be using. Let's start by creating an account and installing the Heroku CLI tool.

- [Sign up to get free Heroku account](https://signup.heroku.com/dc)

- [Install the Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli)(we use this to manage our Heroku applications)

- Install the Heroku Builds plugin for the Heroku CLI (we use this to upload our applications to Heroku):
  ```
  heroku plugins:install heroku-builds
  ```

## Publishing to Heroku

- [Download code and extract it to a new folder.](https://github.com/nicevo/helloworld-klarna/archive/step-heroku.zip)

- Open a console (terminal window) in your project folder and tell Heroku to publish a new application by running this command:
```
heroku apps:create
```
you will get something like:
_Creating app... done, ⬢ fathomless-hamlet-36755
..._
**fathomless-hamlet-36755** is the name of your app. Save that for later. One can also specify a name, but for the tutorial we did not for speed.

- Now Run this to deploy (i.e. publish) your application to Heroku:
```
heroku builds:create --app NAME_OF_YOUR_HEROKU_APPLICATION
heroku ps:scale web=1 --app NAME_OF_YOUR_HEROKU_APPLICATION
```

- You should now be able open a browser and get the current time by visiting <https://NAME_OF_YOUR_HEROKU_APPLICATION.herokuapp.com/time>.
or just type
```
heroku open --app NAME_OF_YOUR_HEROKU_APPLICATION
```

**Congratulations!** You just created a publicly available web service.

Try to open the app from your phone as well. Sure, it's not a bot yet but we'll fix that in the next step.

## Changing the application and updating Heroku

Change something in the code, for example try renaming "time" to "now" in the `@application.route...` line from `app/views.py`, and update the app on heroku:

```
heroku builds:create --app NAME_OF_YOUR_HEROKU_APPLICATION
```
Now the link you have to go to would be `.../now` instead of `.../time`

# Troubleshooting a problem

No response from the bot? Weird errors?

Many problems are never shown to the user but are logged in the application log inside Heroku.

You can look at the logs using this command:

```
heroku logs -t --app NAME_OF_YOUR_HEROKU_APPLICATION
```

The logs might show something like this...

```
2017-02-18T15:04:43.580726+00:00 app[web.1]:
KikError: {"message":"Invalid config","error":"BadRequest"}
2017-02-18T15:04:43.581128+00:00 app[web.1]:
[2017-02-18 15:04:43 +0000] [9] [INFO] Worker exiting (pid: 9)
2017-02-18T15:04:43.610055+00:00 app[web.1]:
[2017-02-18 15:04:43 +0000] [4] [INFO] Shutting down: Master
2017-02-18T15:04:43.610179+00:00 app[web.1]:
[2017-02-18 15:04:43 +0000] [4] [INFO] Reason: Worker failed to boot.
2017-02-18T15:04:43.778824+00:00 heroku[web.1]: State changed from up to crashed
2017-02-18T15:04:43.601251+00:00 heroku[web.1]: State changed from starting to up
2017-02-18T15:04:43.733380+00:00 heroku[web.1]: Process exited with status 3
```

## A Closer Look

More reading about Heroku:

- Heroku Architecture: <https://devcenter.heroku.com/categories/heroku-architecture>
- Python on Heroku: <https://devcenter.heroku.com/articles/getting-started-with-python>
- Heroku CLI cheat sheet: <http://ricostacruz.com/cheatsheets/heroku.html>
- Heroku CLI usage: <https://devcenter.heroku.com/articles/using-the-cli>

## The Next Step

[Go to instructions for Step 3 - Kik](./step-kik.md)

[Go to instructions for Step 3 - Telegram](./step-telegram.md)

[Back to index](./index.md)
