# Käytä Python 3.8 -pohjaa
FROM python:3.11

# Aseta työskentelykansio /app
WORKDIR /app

# Kopioi paikallinen koodi konttiin
COPY . /app

# Asenna riippuvuudet
RUN pip install -r requirements.txt

# Määritä, mitä komentoa käytetään kontin käynnistämiseen
RUN apt update && apt install -y telnet
