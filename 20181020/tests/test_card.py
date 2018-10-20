#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest

from poker.card import Card


@pytest.mark.parametrize('card', [
    '2D',
    '3S',
    '5S'
    ])
def test_repr(card):
    assert repr(Card(card)) == \
            '<Card: {{ value: {}, suit: {} }}>'.format(card[0], card[1])


@pytest.mark.parametrize('card', [
    'XX',
    'J2',
    '2AX',
    '2',
    'X'
])
def test_invalid_card(card):
    with pytest.raises(ValueError):
        Card(card)
