import network
import secrets
import time
import urequests
import time
from neopixel import Neopixel

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(secrets.SSID, secrets.PASSWORD)
while True:
  time.sleep(1)
  if wlan.isconnected() == True:
    print('Wi-Fi Connected!')
    break
  print('Waiting for Wi-Fi connection...')
  time.sleep(1)

pixels = Neopixel(7, 0, 0, "GRB")

while True:
    collections = urequests.get("http://IP_ADDRESS:6000/api/current_bin").json()
    if len(collections) == 0:
        print('NO BIN DATES RETURNED FROM API')
        time.sleep(5)
    else:
        for collection in collections:
            if (collection['bin_colour']) == 'grey':
                print('GREY LIGHT')
                pixels.fill((220,220,220))
                pixels.show()
                time.sleep(5)
            elif (collection['bin_colour']) == 'green':
                print('GREEN LIGHT')
                pixels.fill((0,255,0))
                pixels.show()
                time.sleep(5)
            elif (collection['bin_colour']) == 'brown':
                print('BROWN LIGHT')
                pixels.fill((240,30,5))
                pixels.show()
                time.sleep(5)
            else:
                print('ERROR!')

