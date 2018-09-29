#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
from arabic_to_roman import arabic_to_roman


@pytest.mark.parametrize(
    'roman_number, arabic_number', [
        ('I', 1),
        ('V', 5),
        ('X', 10),
        ('L', 50),
        ('C', 100),
        ('D', 500),
        ('M', 1000)
    ]
)
def test_basic_numbers(roman_number, arabic_number):
    assert roman_number == arabic_to_roman(arabic_number)


@pytest.mark.skip()
@pytest.mark.parametrize(
    'roman_number, arabic_number', [
        ('II', 2),
        ('XX', 20),
        ('CC', 200),
        ('MM', 2000)
    ]
)
def test_equal_numbers(roman_number, arabic_number):
    assert roman_number == arabic_to_roman(arabic_number)


@pytest.mark.skip()
@pytest.mark.parametrize(
    'roman_number, arabic_number', [
        ('VI', 6),
        ('XI', 11),
        ('CV', 105),
        ('MC', 1100)
    ]
)
def test_addition_sequence_numbers(roman_number, arabic_number):
    assert roman_number == arabic_to_roman(arabic_number)


@pytest.mark.skip()
@pytest.mark.parametrize(
    'roman_number, arabic_number', [
        ('IV', 4),
        ('IX', 9),
        ('XCV', 95),
        ('CM', 900)
    ]
)
def test_subtract_sequence_numbers(roman_number, arabic_number):
    assert roman_number == arabic_to_roman(arabic_number)


@pytest.mark.skip()
@pytest.mark.parametrize(
    'roman_number, arabic_number', [
        ('MCMV', 1905),
        ('DIX', 509),
        ('CDLXXXV', 485),
        ('MCMLXXVII', 1977)
    ]
)
def test_complex_sequence_numbers(roman_number, arabic_number):
    assert roman_number == arabic_to_roman(arabic_number)
