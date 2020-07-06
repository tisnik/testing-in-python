#!/usr/bin/env python3
# vim: set fileencoding=utf-8

import requests

# adresa s testovaci REST API sluzbou
URL = "http://httpbin.org/status/500"

# poslani HTTP dotazu typu GET
response = requests.get(URL)

# vypis stavu odpovedi
print(response.status_code)
print(response.ok)
