# Utmaning 1: Lokal webbtjänst

Första steget är att försäkra oss om att vi kan grunderna i att utveckla webbtjänster i Python. Det här kräver Python (och Pip).

Vi börjar med ett exempelprojekt bara för att se så att du har alla nödvändiga bibliotek installerade.

På <https://github.com/mikaelsvensson/helloworld-klarna/tree/challenge-1> hittar du all källkod för övningen. Ja, vi fuskar lite genom att inte skriva någon kod själva men det är mest för att komma igång.

## Steg för steg

1. Ladda ner källkoden härifrån: <https://github.com/nicevo/helloworld-klarna/archive/challenge-1.zip>.
2. Packa upp zip-filen i en ny mapp, exempelvis `helloworld-klarna`.
3. Öppna en kommandoprompt och gå till din projektmapp.
4. Installera biblioteken vi behöver genom att köra detta:

  ```
  pip install -r requirements.txt
  ```

5. Starta webbtjänsten genom att köra detta:

  ```
  python run.py
  ```

6. Öppna <http://localhost:5000/time> i en webbläsare. Detta borde ge dig aktuellt klockslag.

Vi har nu en webbtjänst snurrandes på vår egen dator. Visst, den kan bara användas av någon som sitter vid just denna dator men det fixar vi i nästa steg.

## En närmare titt

Ta lite tid och undersök källkoden. Börja med `run.py`, gå vidare till `app/__init__.py` och titta sedan på `views.py`.

Vi använder Flask, ett webbtjänstbibliotek för Python, och vill du veta mer kan du hitta en ordentlig genomgång på <https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world>.

## Gå vidare

[Gå till instruktionerna för Utmaning 2](./challenge-heroku.sv.md)

[Gå till index](./index.sv.md)
