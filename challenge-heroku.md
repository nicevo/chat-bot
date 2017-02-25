# Challenge 2: Publish to Heroku
 
In order to make our fancy web service (which still only tells the time of the day) available to everyone in the entire world to enjoy we will use the free web service hosting service Heroku. There are paid hosting service on Heroku as well but the free service is more than enough for our needs.

1.  Sign up to get free Heroku account on https://signup.heroku.com/dc

1.  Install the Heroku CLI from 
    https://devcenter.heroku.com/articles/heroku-cli 
    (we use this to manage our Heroku applications)

1.  Install the Heroku Builds plugin for the Heroku CLI (we use this to upload our applications to Heroku):
    
        heroku plugins:install heroku-builds

## Things changed compared to the previous challenge

1.  Create a file called Procfile (no extension, just the name “Procfile”) with this content:
    
        web: gunicorn app:application --log-file -
        
    Note the “-” and the end of the line. Also note that Procfile must be in the root of your project.
    This file tells Heroku how your application is started.

1.  Modify ```requirements.txt``` so that is has these two lines of code:
    
        Flask
        gunicorn
        
1.  Create an empty file named .gitignore the root of your project (note the initial period character). We need this because of a bug in the Heroku Builds plugin (which requires that a file with this exact name exists). On a Mac you can create this file using this console command:
    
        touch .gitignore

1.  Tell Heroku you want to publish a new application by running this in a console:
    
        heroku apps:create A_NAME_OF_YOUR_CHOICE
    
    Same examples:
    
        heroku apps:create boatymcboatface
        heroku apps:create happy-marvin
        
1.  Run this to deploy your application to Heroku:
    
        heroku builds:create -a A_NAME_OF_YOUR_CHOICE

You should now be able open a browser and get the current time by visiting 
https://A_NAME_OF_YOUR_CHOICE.herokuapp.com/time.

If it does not work you may have to run these two commands: 
    
    heroku ps:scale web=1
    heroku open

We have a publicly available web service now! Sure, it’s not a bot yet but we’ll fix that in the next step.

If one does a change to the code, for example renaming “time” to “now”, and redeploy:
    
    heroku builds:create -a A_NAME_OF_YOUR_CHOICE

## Troubleshooting a problem

No response from the bot? Weird errors?

Many problems are never shown to the user but are logged in the application log inside Heroku.

You can look at the logs using this command:

    heroku logs -t --app A_NAME_OF_YOUR_CHOICE

The logs might show something like this…

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

## More reading

* Heroku Architecture: https://devcenter.heroku.com/categories/heroku-architecture
* Python on Heroku: https://devcenter.heroku.com/articles/getting-started-with-python
* Heroku CLI cheat sheet: http://ricostacruz.com/cheatsheets/heroku.html
* Heroku CLI usage: https://devcenter.heroku.com/articles/using-the-cli

## The Next Step

[Go to instructions for Challenge 3 - Kik](./challenge-kik.md)

[Go to instructions for Challenge 3 - Telegram](./challenge-telegram.md)