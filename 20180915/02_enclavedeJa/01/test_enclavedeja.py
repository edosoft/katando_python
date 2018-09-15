#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
from enclavedeja import get_price


@pytest.mark.parametrize(
    'seasons, expected', [
        ([0], 5*1),
        ([0, 1], 5*2),
        ([0, 1, 2], 5*3*.9),
        ([0, 1, 2, 3], 5*4*.9)
    ]
)
def test_no_discount(seasons, expected):
    assert expected == get_price(seasons)


# @pytest.mark.skip()
@pytest.mark.parametrize(
    'seasons, expected', [
        ([0, 1, 2], 5*3*.9),
        ([0, 1, 2, 3], 5*4*.9)
    ]
)
def test_10_percent_discount(seasons, expected):
    assert expected == get_price(seasons)


# @pytest.mark.skip()
@pytest.mark.parametrize(
    'seasons, expected', [
        ([0, 1, 2, 3, 4], 5*5*.8),
        ([0, 0, 1, 2, 3, 4], 5*6*.8)
    ]
)
def test_20_percent_discount(seasons, expected):
    assert expected == get_price(seasons)
