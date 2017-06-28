# Step 1: Local web service

The first step makes sure that we know the basics of how to develop web services using Python. This will only require Python (and Pip). We will start with a sample project just to see that you have all the required libraries installed.

## Step By Step

- [Download the source code](https://github.com/nicevo/helloworld-klarna/archive/step-localhost.zip)
- Extract the zip file to a new folder, such as `helloworld-klarna`.
- Open a **console** and go to your new project folder
- Install the dependencies by executing this:
  ```
  pip install -r requirements.txt
  ```
- Start the service by executing this:
  ```
  python run.py
  ```
- Open `http://localhost:5000/time` in a browser. This should give you the time of the day.

We now have a web service running on your own computer. Sure, it can only be used by someone sitting at your computer but we'll fix that in the next step.

## A Closer Look

Take some time to explore the source code. Start with `run.py`, move on to `app/__init__.py` and then have a look at `views.py`.

We're using Flask, a web service library for Python, and a lot of information about it can be found on <https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world>.

## The Next Step

[Go to instructions for Step 2](./step-heroku.md)

[Back to index](./index.md)
