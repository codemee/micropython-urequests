# micropython-urequests with redirection implemented

The urequests module in MicroPython dowsn't support redirection. I modify the urequests module to make a recursive call to urequests.request when the response header contains a Location item and the HTTP status code is 3XX.
