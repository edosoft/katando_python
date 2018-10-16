#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
from enclavedeja import get_price

THRESHOLD = 0.00001

def similar(a, b):
    """
    Takes two numeric arguments and returns `True` if their difference is
    smaller than certain threshold (making them effectively equal for our
    purposes).

    This is useful when dealing with floating point, because operating
    with the numbers add up rounding errors, and comparing one such result
    to a floating point constant (or a number derived using different
    operations) may result in non-equal numbers.
    """
    return abs(a - b) < THRESHOLD

@pytest.mark.parametrize(
    'seasons, expected', [
        ([0, 1], 3 + 3.5),
        ([2, 3], 4 + 4.5),
        ([0, 0, 0, 0], 3 * 4)
    ]
)
def test_no_discount(seasons, expected):
    assert similar(expected, get_price(seasons))


@pytest.mark.skip()
@pytest.mark.parametrize(
    'seasons, expected', [
        ([0, 1, 2], 9.45),
        ([0, 1, 2, 3], (3 + 3.5 + 4 + 4.5)*.8),
        ([0, 1, 2, 3, 4], (3 + 3.5 + 4 + 4.5 + 5)*.7)
    ]
)
def test_simple_discount(seasons, expected):
    assert similar(expected, get_price(seasons))


@pytest.mark.skip()
@pytest.mark.parametrize(
    'seasons, expected', [
        ([0, 1, 2, 3, 3], (3 + 3.5 + 4 + 4.5)*.8 + 4.5),
        ([0, 1, 2, 3, 1, 2, 3], (3 + 3.5 + 4 + 4.5)*.8 + (3.5 + 4 + 4.5)*.9)
    ]
)
def test_20_percent_discount(seasons, expected):
    assert expected == get_price(seasons)
