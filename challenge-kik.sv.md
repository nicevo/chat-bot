# Utmaning 3: Berätta för chattappföretaget att du finns
 
Vi måste nu berätta för Kik eller Telegram att vi vill programmera en bot för deras plattform 
(dvs. deras app), annars kommer användarna inte kunna hitta boten i appen.

## Steg för steg

1.  Berätta för Kik att du vill skapa en bot
    1.  På telefon:  Starta Kik.
    1.  På dator: Gå till https://dev.kik.com/.
    1.  På telefon: Scanna Kik-koden på Kik-hemsidan.
    1.  På telefon: boten Botsworth kommer börja chatta med dig och fråga vad du vill att din bot ska heta.
    1.  På dator: Klicka på Log in-knappen på Kiks hemsida och scanna Kik-koden med appen. Gå sedan 
        till kontokonfigurationen (fortfarande på datorn) och leta upp din bots "API key" 
        (på https://dev.kik.com/#/engine). API-nyckeln är din bots lösenord.
    1.  På daton: Spara API-nyckeln i en textfil, så att vi kan använda den senare.
    1.  Vi är nu redo att börja utveckla vår Kik-bot! Gå vidare till nästa steg.

1.  Om du _inte har gjort Utmaning 2_ och bara vill göra Utmaning 3 direkt:

    1.  Gör stegen "Kom igång med Heroku" från [Utmaning 2](./challenge-heroku.sv.md).
    
    1.  Ladda ner och packa upp https://github.com/mikaelsvensson/helloworld-klarna/archive/challenge-4-kik.zip 
        till en ny mapp, exempelvis ```helloworld-klarna```.

1.  Om du _redan är klar med Utmaning 2_ och bara vill fortsätta med det projektet:

    1.  Gå till https://github.com/mikaelsvensson/helloworld-klarna/tree/challenge-4-kik för att få "inspiration"
        för de kommande stegen. Kopiera och klistra in så mycket kod som du tycker behövs.
        
    1.  Uppdatera ```requirements.txt```: Rad för Kiks bot-bibliotek. Vi använder det officiella Python-biblioteket från 
        Kik. Se till så att du har denna rad i din requirements.txt: ```kik==1.2.0```
    
    1.  Uppdatera ```app/__init__.py```: Här måste du initiera din bot med din bots användarnamn, din bots 
        lösenord och din bots Heroku-address, dvs. den “callback address” som kommer ta emot alla 
            inkommande meddelanden. Ändra webhook-parametern för att matcha namnet på din Heroku-applikation.
    
    1.  Uppdatera ```app/views.py```: Innehåller funktionaliteten som tar hand om alla inkommande meddelanden.

1.  Ange din bots inloggningsuppgifter (botens användarnamn och API-nyckel är de du tidigare hittade på
    https://dev.kik.com/#/engine) i din Heroku-applikation genom att köra följande kommandon:
    
        heroku config:set KIK_BOT_USERNAME=your-bot-username --app NAMN_PA_DIN_HEROKU_APPLIKATION
        heroku config:set KIK_BOT_APIKEY=your-bot-api-key --app NAMN_PA_DIN_HEROKU_APPLIKATION
 
1.  Ladda upp applikationen till Heroku precis som tidigare:

        heroku builds:create --app NAMN_PA_DIN_HEROKU_APPLIKATION
 
Du bör nu kunna hitta din bot i Kik genom att söka efter namnet du angav till Botsworth tidigare. 
Börja chatta med din bot och kolla så att du får tillbaka allt du skriver.

Exemplet från zip-filen innehåller bara kod för att svara med samma meddelande som skickades till boten, 
så den visar egentligen bara att boten lever. Detta är för övrigt ganska exakt vad Kiks eget bot-exempel 
gör och som du hittar på https://kik.readthedocs.io/en/latest/user.html#example-bot.

Inga svar från din bot? Kolla botens logg mha. detta kommando:
    
    heroku logs -t --app NAMN_PA_DIN_HEROKU_APPLIKATION