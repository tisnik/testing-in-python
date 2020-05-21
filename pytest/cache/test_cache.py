"""Implementace jednotkových testů."""

import pytest


def test_cache(printer, cache):
    counter = cache.get("foobar/counter", 0)
    printer(counter)
    counter += 1
    cache.set("foobar/counter", counter)
