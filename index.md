# How To Develop A Bot

This tutorial enables you to develop a chat bot for either Kik or Telegram.

This is how bots work for both Kik and Telegram:

1. Create a bot account for Kik or Telegram. During this simple process you will get an API key. The API key is the bot's password when talking to the messaging platform (i.e. Kik or Telegram).
2. Implement the messaging platform's bot callback interface as a web service. You then publish this web service on a cloud provider (we will use Heroku in this tutorial).
3. All messages sent to your bot will be delivered to your web service.

There are some things in common regardless of whether or not you go for Kik or Telegram:

- We use a Python library which takes care of "the complicated stuff".
- We create a web service which will receive all the messages sent to our bot.
- We don't specify our bot's credentials in the source code (that way we can publish our source code without divulging the bot's credentials, i.e. its secret password).
- We make sure that the application, i.e. the bot, starts by telling the app company (i.e. Kik or Telegram) that it is alive and can receive messages.

Since Kik and Telegram are different apps there are some things that will be different when you develop a bot for one or the other. For this reason the instructions will differ depending on the app you want to support.

# Software Requirements

You must have this installed on your computer:

- Python 2.7 from <https://www.python.org/downloads>.
- Pip, which we use to install Python libraries. Pip should be bundled with the Python installation. Verify this by executing this command in a terminal/console:

  ```
  pip --version
  ```

  _You can develop a bot without Pip but you have to skip Challenge 1_

- Any IDE with Python support, for example the community edition of PyCharm from <https://www.jetbrains.com/pycharm/download>.

Tools you don't need at this point but might be useful when you develop more complicated chat bots (or any other complicated project for that matter):

- Git from <https://git-scm.com/downloads>.
- Setuptools and Virtualenv, as per <https://packaging.python.org/installing>.

# Challenges

We don't like the words "assignments" or "tasks". Talking about "challenges" sounds more fun.

This tutorial on chat bot development consists of three challenges:

- Challenge 1: Try running a web service on your own computer. This is just to make sure you have all the necessary tools installed on your computer.

  [Go to instructions for Challenge 1](./challenge-localhost.md)

- Challenge 2: Create a web service in "the cloud" and which can be used by anyone in the world.

  [Go to instructions for Challenge 2](./challenge-heroku.md)

- Challenge 3: Create a chat bot, which is actually a web service, which lives in "the cloud". It is either a Kik bot or a Telegram bot.

  [Go to instructions for Challenge 3 - Kik](./challenge-kik.md)

  [Go to instructions for Challenge 3 - Telegram](./challenge-telegram.md)

- Bonus: Let the fun begin!

  [Go to instructions for Quiz](./challenge-quiz.md)
