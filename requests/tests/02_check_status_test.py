#!/usr/bin/env python3
# vim: set fileencoding=utf-8

import requests


def test_get_method_for_existing_endpoint():
    # adresa s testovaci REST API sluzbou
    URL = "http://httpbin.org/get"

    # poslani HTTP dotazu typu GET
    response = requests.get(URL)

    assert response is not None
    assert response.ok
    assert response.status_code == 200


def test_get_method_for_missing_endpoint():
    # adresa s testovaci REST API sluzbou
    URL = "http://httpbin.org/neexistuje"

    # poslani HTTP dotazu typu GET
    response = requests.get(URL)

    assert response is not None
    assert response.ok
    assert response.status_code == 200
