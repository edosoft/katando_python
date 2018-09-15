#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
from enclavedeja import get_price


@pytest.mark.parametrize(
    'seasons, expected', [
        ([0, 1], 2.5 + 3),
        ([2, 3], 3.5 + 4),
        ([0, 0, 0, 0], 2.5 * 4)
    ]
)
def test_no_discount(seasons, expected):
    assert expected == get_price(seasons)


@pytest.mark.skip()
@pytest.mark.parametrize(
    'seasons, expected', [
        ([0, 1, 2], (2.5 + 3 + 3.5)*.9),
        ([0, 1, 2, 3], (2.5 + 3 + 3.5 + 4)*.8),
        ([0, 1, 2, 3, 4], (2.5 + 3 + 3.5 + 4 + 4.5)*.7),
        ([0, 1, 2, 3, 4, 5], (2.5 + 3 + 3.5 + 4 + 4.5)*.7 + 5)
    ]
)
def test_simple_discount(seasons, expected):
    assert expected == get_price(seasons)


@pytest.mark.skip()
@pytest.mark.parametrize(
    'seasons, expected', [
        ([0, 1, 2, 3, 3], (2.5 + 3 + 3.5 + 4)*.8 + 4),
        ([0, 1, 2, 3, 1, 2, 3], (2.5 + 3 + 3.5 + 4)*.8 + (3 + 3.5 + 4)*.9),
        ([0, 1, 2, 3, 5, 1, 2, 3, 5],
         (2.5 + 3 + 3.5 + 4)*.7 + (3 + 3.5 + 4)*.8 + 5*2),
        ([0, 1, 2, 3, 5, 1, 2, 3],
         (2.5 + 3 + 3.5 + 4)*.7 + (3 + 3.5 + 4)*.9 + 5)
    ]
)
def test_multiple_discount(seasons, expected):
    assert expected == get_price(seasons)
