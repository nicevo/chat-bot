# How To Develop A Bot

This tutorial enables you to develop a chat bot for either Kik or Telegram.
[Check the prerequisites](./step-prerequisites.md)

# Steps

In development one tries to split the tasks in smaller pieces to be able to focus on one thing at a time. 

This tutorial on chat bot development is split in three steps:

## Step 1 - Localhost  

Try running a web service on your own computer. This is just to make sure you have all the necessary tools installed on your computer.

  [Go to instructions for Step 1](./step-localhost.md)

## Step 2 - Web service on Heroku

Create a web service in "the cloud" and which can be used by anyone in the world.

  [Go to instructions for Step 2](./step-heroku.md)

## Step 3 - Create chat bot 

Create a chat bot, which is actually a web service, which lives in "the cloud". It is either a Kik bot or a Telegram bot.
Since Kik and Telegram are different apps there are some things that will be different when you develop a bot for one or the other. For this reason the instructions will differ depending on the app you want to support.

  [Go to instructions for Step 3 - Kik](./step-kik.md)

  [Go to instructions for Step 3 - Telegram](./step-telegram.md)

There are some things in common regardless of whether or not you go for Kik or Telegram:

- We use a Python library which takes care of interacting with the bot.
- We create a web service which will receive all the messages sent to our bot.
- We don't specify our bot's credentials in the source code (that way we can publish our source code without divulging the bot's credentials, i.e. its secret password).
- We make sure that the application, i.e. the bot, starts by telling the app company (i.e. Kik or Telegram) that it is alive and can receive messages.

# Let the fun begin!

We compiled some ideas of chat bots that you can try to implement!
  [Go to ideas on chat bots](./bots-ideas.md)

# Extras

Tools you don't need at this point but might be useful when you develop more complicated chat bots (or any other complicated project for that matter):

- Git from <https://git-scm.com/downloads>.
- Setuptools and Virtualenv, as per <https://packaging.python.org/installing>.

