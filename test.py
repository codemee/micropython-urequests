import network
import urequests_alt

sta = network.WLAN(network.STA_IF)
sta.active(True)
sta.connect('MEE_MI', 'PinkFloyd1969')
while not sta.isconnected():
    pass

r = urequests_alt.get('http://flagtech.github.io/flag.txt')
print(r.status_code)
print(r.text)