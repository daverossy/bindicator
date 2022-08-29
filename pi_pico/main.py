import network
import secrets
import time
import urequests
import time
from neopixel import Neopixel

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(secrets.SSID, secrets.PASSWORD)
#print(wlan.isconnected())

pixels = Neopixel(7, 0, 0, "RGBW")

while True:
    collections = urequests.get("http://IP_ADDRESS:6000/api/current_bin").json()
    if len(collections) == 0:
        print('NO BIN DATES RETURNED FROM API')
        time.sleep(5)
    else:
        for collection in collections:
            if (collection['bin_colour']) == 'grey':
                print('GREY LIGHT')
                pixels.fill((169,169,169))
                time.sleep(5)
            elif (collection['bin_colour']) == 'green':
                print('GREEN LIGHT')
                pixels.fill((50,205,50))
                time.sleep(5)
            elif (collection['bin_colour']) == 'brown':
                print('BROWN LIGHT')
                pixels.fill((165, 42, 42))
                time.sleep(5)
            else:
                print('ERROR!')
