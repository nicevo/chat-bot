# Berätta för chattappföretaget att du finns
 
Vi måste nu berätta för Kik eller Telegram att vi vill programmera en bot för deras plattform (dvs. deras app), annars kommer användarna inte kunna hitta boten i appen.

Berätta för Telegram att du vill skapa en bot

1.  På telefon: Starta Telegram.
1.  På telefon: Börja chatta med BotFather.
1.  På telefon: Svara på frågorna från BotFather.
1.  På telefon: Efter ett par frågor får du ett meddelande som börjar med “Done! Congratulations…”. Detta meddelande kommer innehålla din API-nyckel.
1.  På daton: Spara API-nyckeln i en textfil, så att vi kan använda den senare.
 
Vi är nu redo att börja utveckla vår Telegram-bot!

Hämta källkoden från https://github.com/mikaelsvensson/helloworld-klarna/archive/challenge-4-telegram.zip, eller fortsätt med ditt tidigare projekt.

Zip-filen ger dig följande nyheter:
*   ```requirements.txt```: Nytt beroende till Python-bibliotek för Telegram.
*   ```app/__init__.py```: Initiera boten med din bots inloggningsuppgifter (en API-nyckel).
*   ```app/views.py```: Funktionaliteten som tar hand om alla meddelanden som skickas till vår callback-adress. Exemplet från zip-filen svarar bara med vad som skickades, så det visar i princip bara att boten lever.
*   ```init_webhook.py```: Separat Python-skript som berättar för Telegram om vår webbtjänsts adress, dvs. callback-adressen som Telegram ska skicka inkommande meddelanden till. Ändra webhook-parametern för att matcha din Heroku-apps namn.
*   ```Procfile```: Kör init_webhook.py och först därefter själva bot-webbtjänsten.
*   ```ssl-certificate.herokuapp-com.pem```: https-certifikat som används för kryptering.

Kolla så att du har rätt beroenden (Python-paket) installerade. Det finns flera bibliotek (paket) för att 
skapa Telegram-botar och vi kommer använda ett som heter twx.botapi.

Kontrollera att du har denna rad i din requirements.txt:
    
    twx.botapi==3.1.1
 
Öppna init_webhook.py och kontrollera att adressen i set_webhook-anropet matchar namnet på din applikation.

Spara din bots inloggningsuppgift (dvs. API-nyckeln du fick från BotFather) i din Heroku-applikation med detta kommando:
    
    heroku config:set TELEGRAM_BOT_APIKEY=your-bot-api-key

Lägg till --app A_NAME_OF_YOUR_CHOICE i slutet av ovanstående kommando om du har flera Heroku-applikationer.

Ladda upp applikationen till Heroku precis som tidigare:
    
    heroku builds:create -a A_NAME_OF_YOUR_CHOICE
 
Du bör nu kunna hitta din bit i Telegram genom att söka efter namnet du angav till BotFather 
tidigare. Börja chatta med din bot och kolla så att du får tillbaka allt du skriver.
​
Vill du veta mer om Telegram-botar? Kolla in https://core.telegram.org/bots.

Det var allt, eller kanske bara början!?

Du har nu en fullt fungerande bot. Den gör inte så mycket ännu, så nu är det upp till dig att göra den till något fantastiskt!
