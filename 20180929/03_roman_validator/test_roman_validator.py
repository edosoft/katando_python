#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
from roman_validator import roman_validator


@pytest.mark.parametrize(
    'roman_number', [
        'XLV',
        'CDXCV',
        'CDL',
        'IV',
        'IX',
        'XL',
        'XC',
        'CD',
        'CM'
    ]
)
def test_valid_roman_numbers(roman_number):
    assert roman_validator(roman_number)


@pytest.mark.parametrize(
    'roman_number', [
        'VL',
        'VD',
        'LD',
        'IIII',
        'VIV',
        'XXXX',
        'LXL',
        'CCCC',
        'DCD'
    ]
)
def test_invalid_roman_numbers(roman_number):
    assert not roman_validator(roman_number)
