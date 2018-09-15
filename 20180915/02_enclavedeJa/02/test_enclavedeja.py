#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
from enclavedeja import get_price


@pytest.mark.parametrize(
    'seasons, expected', [
        ([0, 1], 3 + 3.5),
        ([2, 3], 4 + 4.5),
        ([0, 0, 0, 0], 3 * 4)
    ]
)
def test_no_discount(seasons, expected):
    assert expected == get_price(seasons)


# @pytest.mark.skip()
@pytest.mark.parametrize(
    'seasons, expected', [
        ([0, 1, 2], 9.45),
        ([0, 1, 2, 3], (3 + 3.5 + 4 + 4.5)*.8),
        ([0, 1, 2, 3, 4], (3 + 3.5 + 4 + 4.5 + 5)*.7)
    ]
)
def test_simple_discount(seasons, expected):
    assert expected == get_price(seasons)


# @pytest.mark.skip()
@pytest.mark.parametrize(
    'seasons, expected', [
        ([0, 1, 2, 3, 3], (3 + 3.5 + 4 + 4.5)*.8 + 4.5),
        ([0, 1, 2, 3, 1, 2, 3], (3 + 3.5 + 4 + 4.5)*.8 + (3.5 + 4 + 4.5)*.9)
    ]
)
def test_20_percent_discount(seasons, expected):
    assert expected == get_price(seasons)
