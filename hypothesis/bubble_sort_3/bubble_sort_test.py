"""Test naivního algoritmu bublinkového řazení."""

from hypothesis import given
from hypothesis.strategies import lists, integers

from bubble_sort import bubble_sort


@given(lists(integers()))
def test_bubble_sort(alist):
    assert bubble_sort(alist) == sorted(alist)
