#!/usr/bin/env python
# vim: set fileencoding=utf-8

#
#  (C) Copyright 2018  Pavel Tisnovsky
#
#  All rights reserved. This program and the accompanying materials
#  are made available under the terms of the Eclipse Public License v1.0
#  which accompanies this distribution, and is available at
#  http://www.eclipse.org/legal/epl-v10.html
#
#  Contributors:
#      Pavel Tisnovsky
#

from behave import given, then, when


@given('The library {library_name} is loaded')
def initial_state(context, library_name):
    context.load_library(context, library_name)


@when('I call native function add with arguments {x:d} and {y:d}')
def call_add(context, x, y):
    context.result = context.tested_library.add(x, y)


@then('I should get {result:d} as a result')
def check_integer_result(context, result):
    assert context.result == result, \
            "Expected result: {e}, returned value: {r}".format(e=result, r=context.result)
