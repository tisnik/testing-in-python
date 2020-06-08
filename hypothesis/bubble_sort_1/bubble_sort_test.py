"""Test naivního algoritmu bublinkového řazení."""

from bubble_sort import bubble_sort


def test_bubble_sort_empty_input():
    """Test naivního algoritmu bublinkového řazení."""
    assert bubble_sort([]) == []


def test_bubble_sort_one_item():
    """Test naivního algoritmu bublinkového řazení."""
    assert bubble_sort([1]) == [1]


def test_bubble_sort_two_items():
    """Test naivního algoritmu bublinkového řazení."""
    assert bubble_sort([1, 2])
    assert bubble_sort([2, 1])


def test_bubble_sort_four_items():
    """Test naivního algoritmu bublinkového řazení."""
    assert bubble_sort([1, 2, 3, 4])
    assert bubble_sort([1, 2, 4, 3])
    assert bubble_sort([1, 4, 3, 2])
    assert bubble_sort([4, 3, 2, 1])


def test_bubble_sort_five_items():
    """Test naivního algoritmu bublinkového řazení."""
    assert bubble_sort([1, 5, 4, 3, 2])
    assert bubble_sort([5, 4, 3, 2, 1])
