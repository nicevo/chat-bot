# Hur man gör en bot

Den här guiden hjälper dig att skapa en chatbot för Kik eller Telegram.

Några saker är sant för både Kik- och Telegram-botar:

*   Vi använder Python-bibliotek för att ta hand om "de komplicerade sakerna".
*   Vi skapar en webbtjänst som tar emot alla meddelanden som skickas till vår bot.
*   Vi anger inte vår bots lösenord (API-nyckeln) i källkoden (på detta sätt kan vi ge vår källkod till vem som helst utan att avslöja några hemligheter).
*   Boten startar alltid med att berätta för app-företaget (dvs. Kik eller Telegram) att den lever och kan ta emot meddelanden.

# Systemkrav

För att kunna hänga med den måste du har följande på din dator: 
*   Python 2.7 från https://www.python.org/downloads.
*   Pip, som vi använder för att installera Python-bibliotek. Pip bör följa med på köpet när du installerat Python.
    Kontrollera detta genom att köra detta kommando i en termina/kommandotolk:
    
        pip --version

*   Any IDE with Python support, for example the community edition of PyCharm from https://www.jetbrains.com/pycharm/download. 

Verktyg som du inte behöver just nu men som kan vara användbara när du börjar utveckla
mer avancerade botar (eller avancerade projekt i största allmänhet):
*   Git från https://git-scm.com/downloads.
*   Setuptools och Virtualenv, enligt instruktioner på https://packaging.python.org/installing.

# Utmaningar

Ord som "uppgift" eller "övning" låter tråkiga. Ordet "utmaning" låter bättre och roligare.

Den här guiden består av tre utmaningar:

*   Utmaning 1: Skapa en webbtjänst som körs på din egen dator. Det här är mest för att kolla så
    att du har alla nödvändiga verktyg installerade på din dator.

    [Gå till instruktionerna för Utmaning 1](./challenge-localhost.sv.md)

*   Utmaning 2: Skapa en webbtjänst som körs "i molnet" och som vem som helst i hela världen kan se.
    
    [Gå till instruktionerna för Utmaning 2](./challenge-heroku.sv.md)
    
*   Utmaning 3: Skapa en chatbot, som är en webbjänst, som lever "i molnet". Antingen är den för 
    Kik eller för Telegram.
    
    [Gå till instruktionerna för Utmaning 3 - Kik](./challenge-kik.sv.md)
    
    [Gå till instruktionerna för Utmaning 3 - Telegram](./challenge-telegram.sv.md)