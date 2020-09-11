#!/usr/bin/env python3
# vim: set fileencoding=utf-8

import requests

# adresa s testovaci REST API sluzbou
URL = "http://httpbin.org/status/500"

# poslani HTTP dotazu typu GET
response = requests.get(URL)

# precteni hlavicek
headers = response.headers

# vypis typu internetoveho media
print(headers.get("content-type"))

# tento koncový bod vrací obrázek
URL = "http://httpbin.org/image/png"

# poslani HTTP dotazu typu GET
response = requests.get(URL)

# precteni hlavicek
headers = response.headers

# vypis typu internetoveho media
print(headers.get("content-type"))
