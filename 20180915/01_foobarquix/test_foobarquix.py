#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
from foobarquix import foobarquix


@pytest.mark.parametrize(
    'number, expected', [
        (1, '1'),
        (2, '2'),
        (4, '4'),
        (8, '8'),
        (11, '11')
    ]
)
def test_no_match(number, expected):
    assert expected == foobarquix(number)


# @pytest.mark.skip()
@pytest.mark.parametrize(
    'number, expected', [
        (6, 'Foo'),
        (10, 'Bar'),
        (14, 'Quix')
    ]
)
def test_is_divisible_only_by_three_or_five_or_seven(number, expected):
    assert expected == foobarquix(number)


# @pytest.mark.skip()
@pytest.mark.parametrize(
    'number, expected', [
        (13, 'Foo'),
        (52, 'Bar'),
        (17, 'Quix')
    ]
)
def test_only_contains_once_three_or_five_or_seven(number, expected):
    assert expected == foobarquix(number)


# @pytest.mark.skip()
@pytest.mark.parametrize(
    'number, expected', [
        (3, 'FooFoo'),
        (5, 'BarBar'),
        (7, 'QuixQuix'),
    ]
)
def test_only_divisible_once_by_a_number_and_contain_it(number, expected):
    assert expected == foobarquix(number)


# @pytest.mark.skip()
@pytest.mark.parametrize(
    'number, expected', [
        (33, 'FooFooFoo'),
        (15, 'FooBarBar'),
        (35, 'BarQuixFooBar'),
        (63, 'FooQuixFoo')
    ]
)
def test_multiples_matches(number, expected):
    assert expected == foobarquix(number)
