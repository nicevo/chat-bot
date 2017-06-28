# Bot ideas

Here are some ideas of bots and what one could use to create them.

## Calculator bot

A bot that when given an operation it solves it.
e.g.
```
4*10
```
the bot should respond
```
40
```
if the mesage does not match `<number><operation><number>` then it should say:
```
I am sorry <username>, I cannot calculate that :(
```

See [regular expressions](https://docs.python.org/3/howto/regex.html)

## Basic Quiz bot 

Have the bot ask a question. 
e.g. 
```
How old is the Python programming language?
```
then using [Kik keyboard](http://kik.readthedocs.io/en/latest/api.html#keyboards-and-responses) or [Telegram Keyboards](https://core.telegram.org/bots#keyboards) one can provide the answer options.
e.g. 
```
"options":["2 years", "8 years", "12 years", "26 years"]
```

It will ask the question until you get it correctly.

Advanced version, will ask new question when you get this one correctly.

## Intelligent bot
Get inspired by Watson Services!
Check out the CodeAcademy class [Learn the Watson API](https://www.codecademy.com/courses/ibm-watson/lessons/working-app/exercises/wdc-overview) and use that to combine AI and your bot!

## The sky is the limit! 
What else would you do with a chat bot? 

[Back to index](./index.md)
