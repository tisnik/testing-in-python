#!/usr/bin/env python3
# vim: set fileencoding=utf-8

import requests
import json


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


def expect_cookie(response, name, value):
    cookies = session.cookies
    assert name in cookies
    assert cookies[name] == value


def expect_cookies(response, how_many):
    cookies = session.cookies
    assert len(cookies) == how_many


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


def set_cookie(session, name, value):
    # adresa s testovaci REST API sluzbou
    URL = "http://httpbin.org/cookies/set/{name}/{value}".format(name=name, value=value)

    # hlavicka posilana v dotazu
    headers = {'accept': 'application/json'}

    # poslani HTTP dotazu typu GET
    return session.get(URL, headers=headers)


def delete_cookie(session, name):
    # adresa s testovaci REST API sluzbou
    URL = "http://httpbin.org/cookies/delete?{name}=".format(name=name)

    # hlavicka posilana v dotazu
    headers = {'accept': 'application/json'}

    # poslani HTTP dotazu typu GET
    return session.get(URL, headers=headers)


def setup_module(module):
    module.session = requests.Session()


def test_set_cookie_1():
    response = set_cookie(session, "foo", "6")

    # zakladni test odpovedi
    expect_ok_response(response)
    expect_content_type(response, "application/json")

    # test cookies
    expect_cookies(response, 1)
    expect_cookie(response, "foo", "6")


def test_set_cookie_2():
    response = set_cookie(session, "bar", "7")

    # zakladni test odpovedi
    expect_ok_response(response)
    expect_content_type(response, "application/json")

    # test cookies
    expect_cookies(response, 2)
    expect_cookie(response, "foo", "6")
    expect_cookie(response, "bar", "7")


def test_set_cookie_3():
    response = set_cookie(session, "foo", "42")

    # zakladni test odpovedi
    expect_ok_response(response)
    expect_content_type(response, "application/json")

    # test cookies
    expect_cookies(response, 2)
    expect_cookie(response, "foo", "42")
    expect_cookie(response, "bar", "7")


def test_delete_cookie_1():
    response = delete_cookie(session, "foo")

    # zakladni test odpovedi
    expect_ok_response(response)
    expect_content_type(response, "application/json")

    # test cookies
    expect_cookies(response, 1)
    expect_cookie(response, "bar", "7")


def test_delete_cookie_2():
    response = delete_cookie(session, "baz")

    # zakladni test odpovedi
    expect_ok_response(response)
    expect_content_type(response, "application/json")

    # test cookies
    expect_cookies(response, 1)
    expect_cookie(response, "bar", "7")


def test_delete_cookie_3():
    response = delete_cookie(session, "bar")

    # zakladni test odpovedi
    expect_ok_response(response)
    expect_content_type(response, "application/json")

    # test cookies
    expect_cookies(response, 0)
