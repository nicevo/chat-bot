# Utmaning 2: Publicera på Heroku
 
För att vår fina webbtjänst (som fortfarande bara berättar vad klockan är) ska kunna avnjutas av alla i hela världen så ska vi använda en gratis molntjänst som heter Heroku. Det finns betaltjänster på Heroku men gratisvarianten räcker mer än väl för våra behov.

1.  Skapa dig ett gratis Heroku-konto på https://signup.heroku.com/dc

1.  Installera Heroku-verktygen från 
    https://devcenter.heroku.com/articles/heroku-cli
    (vi kommer använda detta för att arbeta med vår Heroku-app)

1.  Installera tillägget Heroku Builds för Heroku-verktygen (används för att ladda upp vår app till Heroku):
    
        heroku plugins:install heroku-builds

## Ändringar jämfört med förra uppgiften:

1.  Skapa en fil som heter Procfile (ingen filändelse, bara “Procfile”) med följande innehåll:
    
        web: gunicorn app:application --log-file -
        
    Notera “-” sist på raden. Notera också att Procfile måste finns i "roten" på ditt projekt. 
    Procfile berättar för Heroku hur vår webbtjänst startas.

1.  Ändra ```requirements.txt``` så att den har dessa två rader:

        Flask
        gunicorn

1.  Skapa en tom file som heter .gitignore i "roten" på ditt projekt (notera punkten i början på filnamnet). Vi behöver denna fil pga. en bugg i verktygt Heroku Builds plugin (som alltså kräver att det finns en fil med just detta namn). På en Mac kan du skapa filen med det här terminalkommandot:

        touch .gitignore

1.  Skapa en ny applikation på Heroku mha. detta kommando:

        heroku apps:create A_NAME_OF_YOUR_CHOICE
    
    Några exempel:
    
        heroku apps:create boatymcboatface
        heroku apps:create happy-marvin

1.  Kör det här kommandot för att ladda upp, och starta, din app:
    
        heroku builds:create -a A_NAME_OF_YOUR_CHOICE

Du borde nu kunna öppna en webbläsare och få redan på vad klockan är genom att surfa till
https://A_NAME_OF_YOUR_CHOICE.herokuapp.com/time.

Om det inte fungerar kan du behöva köra dessa kommandon:

    heroku ps:scale web=1
    heroku open
    
Vi har nu en publik webbtjänst som hela världen kan använda! Visst, det är inte en chatbot ännu men det fixar vi i nästa steg!

Pröva att ändra något i koden, exempelvis byta ut "time" mot "now", och ladda upp den nya versionen med samma kommando som tidigare:
    
    heroku builds:create -a A_NAME_OF_YOUR_CHOICE

## Felsöka ett problem

Inget svar från din bot? Konstiga felmeddelanden?

Många fel visas aldrig för användaren men loggas i applikationsloggen i Heroku.

Du kan titta på loggar med det här kommandot:

    heroku logs -t --app A_NAME_OF_YOUR_CHOICE

Loggen kan se ut något i den här stilen...

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

## Mer läsning för den nyfikne

* Herokus arkitektur och struktur: https://devcenter.heroku.com/categories/heroku-architecture
* Python på Heroku: https://devcenter.heroku.com/articles/getting-started-with-python
* "Fuskpapper" för Heroku-verktygen: http://ricostacruz.com/cheatsheets/heroku.html
* Mer information om Heroku-verktygen: https://devcenter.heroku.com/articles/using-the-cli
