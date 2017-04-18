# Utmaning 3: Berätta för chattappföretaget att du finns

Vi måste nu berätta för Kik eller Telegram att vi vill programmera en bot för deras plattform (dvs. deras app), annars kommer användarna inte kunna hitta boten i appen.

- Berätta för Telegram att du vill skapa en bot

  - På telefon: Starta Telegram.
  - På telefon: Börja chatta med BotFather.
  - På telefon: Svara på frågorna från BotFather.
  - På telefon: Efter ett par frågor får du ett meddelande som börjar med "Done! Congratulations...". Detta meddelande kommer innehålla din API-nyckel (dvs. din bots lösenord).
  - På daton: Spara API-nyckeln i en textfil, så att vi kan använda den senare.
  - Vi är nu redo att börja utveckla vår Telegram-bot!

- Om du _inte har gjort Utmaning 2_ och bara vill göra Utmaning 3 direkt:

  - Gör stegen "Kom igång med Heroku" från [Utmaning 2](./challenge-heroku.sv.md).

  - Ladda ner och packa upp <https://github.com/nicevo/helloworld-klarna/archive/challenge-4-telegram.zip> till en ny mapp, exempelvis `helloworld-klarna`.

- Om du _redan är klar med Utmaning 2_ och bara vill fortsätta med det projektet:

  - Gå till <https://github.com/nicevo/helloworld-klarna/tree/challenge-4-telegram> för att få "inspiration" för de kommande stegen. Kopiera och klistra in så mycket kod som du tycker behövs.

  - Uppdatera `app/__init__.py`: Initiera boten med din bots inloggningsuppgifter (en API-nyckel).

  - Uppdatera`app/views.py`: Funktionaliteten som tar hand om alla meddelanden som skickas till vår callback-adress. Exemplet från zip-filen svarar bara med vad som skickades, så det visar i princip bara att boten lever.

  - Skapa `init_webhook.py`: Separat Python-skript som berättar för Telegram om vår webbtjänsts adress, dvs. callback-adressen som Telegram ska skicka inkommande meddelanden till. Ändra `webhook`-parametern för att matcha din Heroku-apps namn.

  - Uppdatera `Procfile`: Kör `init_webhook.py` och först därefter själva bot-webbtjänsten.

  - Skapa `ssl-certificate.herokuapp-com.pem`: https-certifikat som används för kryptering.

- Kolla så att du har rätt beroenden (Python-paket) installerade. Det finns flera bibliotek (paket) för att skapa Telegram-botar och vi kommer använda ett som heter twx.botapi.

  Kontrollera att du har denna rad i din requirements.txt:

  ```
  twx.botapi==3.1.1
  ```

- Öppna `init_webhook.py` och kontrollera att adressen i `set_webhook`-anropet matchar namnet på din applikation.

- Spara din bots inloggningsuppgift (dvs. API-nyckeln du fick från BotFather) i din Heroku-applikation med detta kommando:

  ```
  heroku config:set TELEGRAM_BOT_APIKEY=your-bot-api-key --app NAMN_PA_DIN_HEROKU_APPLIKATION
  ```

- Ladda upp applikationen till Heroku precis som tidigare:

  ```
  heroku builds:create --app NAMN_PA_DIN_HEROKU_APPLIKATION
  ```

Du bör nu kunna hitta din bit i Telegram genom att söka efter namnet du angav till BotFather tidigare. Börja chatta med din bot och kolla så att du får tillbaka allt du skriver. ​

## En närmare titt

Vill du veta mer om Telegram-botar? Kolla in <https://core.telegram.org/bots>.

Det var allt, eller kanske bara början!?

Du har nu en fullt fungerande bot. Den gör inte så mycket ännu, så nu är det upp till dig att göra den till något fantastiskt!

[Gå till index](./index.sv.md)
