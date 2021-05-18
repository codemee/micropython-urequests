import network
import flag_urequests

sta = network.WLAN(network.STA_IF)
sta.active(True)
sta.connect('MEE_MI', 'PinkFloyd1969')
while not sta.isconnected():
    pass

r = flag_urequests.get('http://www.thunderclient.io')
print(r.status_code)
print(r.text)