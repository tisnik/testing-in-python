#!/usr/bin/env python3
# vim: set fileencoding=utf-8

import requests


def expect_ok_response(response):
    assert response is not None
    assert response.ok
    assert response.status_code == 200


def expect_content_type(response, content_type):
    # precteni hlavicek
    headers = response.headers

    # test existence hlavicky
    assert "content-type" in headers

    # kontrola obsahu hlavicky
    assert headers["content-type"] == content_type


def get_value_using_path(obj, path):
    """Get the attribute value using the XMLpath-like path specification.
    Return any attribute stored in the nested object and list hierarchy using
    the 'path' where path consists of:
        keys (selectors)
        indexes (in case of arrays)
    separated by slash, ie. "key1/0/key_x".
    Usage:
    get_value_using_path({"x" : {"y" : "z"}}, "x"))   -> {"y" : "z"}
    get_value_using_path({"x" : {"y" : "z"}}, "x/y")) -> "z"
    get_value_using_path(["x", "y", "z"], "0"))       -> "x"
    get_value_using_path(["x", "y", "z"], "1"))       -> "y"
    get_value_using_path({"key1" : ["x", "y", "z"],
                          "key2" : ["a", "b", "c", "d"]}, "key1/1")) -> "y"
    get_value_using_path({"key1" : ["x", "y", "z"],
                          "key2" : ["a", "b", "c", "d"]}, "key2/1")) -> "b"
    """
    keys = path.split("/")
    for key in keys:
        if key.isdigit():
            obj = obj[int(key)]
        else:
            obj = obj[key]
    return obj


def test_get_method_for_existing_endpoint():
    # adresa s testovaci REST API sluzbou
    URL = "http://httpbin.org/get?x=6&y=7&answer=42"

    # poslani HTTP dotazu typu GET
    response = requests.get(URL)

    # zakladni test odpovedi
    expect_ok_response(response)
    expect_content_type(response, "application/json")

    # ziskani konkretniho prvku z vracene datove struktury
    encoded = response.json()

    answer = get_value_using_path(encoded, "args/answer")
    assert answer == "42"
