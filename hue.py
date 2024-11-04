import requests
import random

# API-avain ja palvelimen osoite
api_key = 'xlVA2fOWBCK39bx2-0OGHPjaNRd5USFON89agOBN'  # HYTELI-reititin
# server_addr = 'http://10.50.91.19'
# server_addr = 'http://172.31.37.17'
server_addr = 'http://128.214.254.124:8181'  # Jaakko
lights = ['1', '2', '3', '4', '5', '6']

class HueHue:

    def __init__(self):
        print("HueHue luotu")

    def randomColor(self):
        bri = 1 + random.randint(0, 254)
        ct = 153 + random.randint(0, 347)
        self._setLights(True, bri, ct)

    def lightsOn(self):
        self._setLights(True, 100, 250)

    def lightsOff(self):
        self._setLights(False, 1, 250)

    def _setLights(self, state, brightness, colortemp):
        print("state:", state)
        if not isinstance(state, bool):
            print("Virheellinen tila-arvo (" + str(state) + "), oletusarvoisesti käytetään 'True'")
            state = True

        if brightness < 1 or brightness > 254:
            print("Kirkkaus ylittää sallitut rajat 1-254, oletusarvoisesti käytetään 50")
            brightness = 50

        if colortemp < 153 or colortemp > 500:
            print("Värimäärä ylittää sallitut rajat 153-500, oletusarvoisesti käytetään 250")
            colortemp = 250

        for light in lights:
            response = requests.put(
                f'{server_addr}/api/{api_key}/lights/{light}/state',
                json={
                    "on": state,  # True / False
                    "bri": brightness,  # 1 - 254
                    "ct": colortemp,  # 153 - 500
                }
            )
            print(response.json())

# Luo HueHue-olio ja käytä sitä
# hue = HueHue()
# hue.lightsOn()

# Lopuksi viesti käyttäjälle siitä, että moduuli on saatavilla muissa tiedostoissa
