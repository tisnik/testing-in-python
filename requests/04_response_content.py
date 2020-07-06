#!/usr/bin/env python3
# vim: set fileencoding=utf-8

import requests

# adresa s testovaci REST API sluzbou
URL = "http://httpbin.org/get?x=6&y=7&answer=42"

# poslani HTTP dotazu typu GET
response = requests.get(URL)

# vypis tela odpovedi
print("Plain text:")
print("-" * 60)
print(response.text)
print("-" * 60)
