# Challenge 2: Publish to Heroku

In order to make our fancy web service (which still only tells the time of the day) available to everyone in the entire world to enjoy we will use the free web service hosting service Heroku. There are paid hosting service on Heroku as well but the free service is more than enough for our needs.

## Step By Step

### Getting started with Heroku

Heroku is the cloud platform we will be using. Let's start by creating an account and installing the Heroku CLI tool.

1. Sign up to get free Heroku account on <https://signup.heroku.com/dc>

1. Install the Heroku CLI from <https://devcenter.heroku.com/articles/heroku-cli> (we use this to manage our Heroku applications)

1. Install the Heroku Builds plugin for the Heroku CLI (we use this to upload our applications to Heroku):

  ```
  heroku plugins:install heroku-builds
  ```

### Publishing to Heroku

**Note**: If you _have not completed Challenge 1_ you'll need to download code from here <https://github.com/nicevo/helloworld-klarna/archive/challenge-2.zip> and extract it to a new folder, for example `helloworld-klarna`.

1. Open a console (terminal window) in your project folder and tell Heroku to publish a new application by running this command:
```
heroku apps:create NAME_OF_YOUR_HEROKU_APPLICATION
```
Choose your own in place of `NAME_OF_YOUR_HEROKU_APPLICATION`, for example:
```
heroku apps:create boatymcboatface
heroku apps:create happy-marvin
```

1. Now Run this to deploy (i.e. publish) your application to Heroku:
```
heroku builds:create --app NAME_OF_YOUR_HEROKU_APPLICATION
heroku ps:scale web=1
```

1. You should now be able open a browser and get the current time by visiting <https://NAME_OF_YOUR_HEROKU_APPLICATION.herokuapp.com/time>.
or just type
```
heroku open
```

Congratulations! You just created a publicly available web service.

Try to open the app from your phone as well. Sure, it's not a bot yet but we'll fix that in the next step.

### Chaning the application and updating Heroku

Change something in the code, for example try renaming "time" to "now" in the `@application.route...` line, and update the app on heroku:

```
heroku builds:create --app NAME_OF_YOUR_HEROKU_APPLICATION
```

## Troubleshooting a problem

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

[Go to instructions for Challenge 3 - Kik](./challenge-kik.md)

[Go to instructions for Challenge 3 - Telegram](./challenge-telegram.md)

[Back to index](./index.md)
