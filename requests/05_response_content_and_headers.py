#!/usr/bin/env python3
# vim: set fileencoding=utf-8

import requests

# adresa s testovaci REST API sluzbou
URL = "http://httpbin.org/get?x=6&y=7&answer=42"

# poslani HTTP dotazu typu GET
response = requests.get(URL)

# precteni hlavicek
headers = response.headers

print("Metadata:")
print("-" * 60)

# vypis typu internetoveho media
print("Typ dat:", headers.get("content-type"))

# vypis delky dat predanych v tele
print("Delka dat:", headers.get("content-length"))

# vypis delky dat predanych v tele
print("Datum:", headers.get("date"))

print("-" * 60)

# vypis tela odpovedi
print("Plain text:")
print("-" * 60)
print(response.text)
print("-" * 60)
