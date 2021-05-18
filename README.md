# micropython-urequests with redirection implemented

The urequests [module](https://github.com/micropython/micropython-lib/tree/master/urequests) in MicroPython doesn't support redirection. I modify the urequests module to make a **recursive call** to `urequests.request` when the response header contains a Location item and the HTTP status code is 3XX.
