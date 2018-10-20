#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest

from poker.hand import Hand
from poker.game import play


@pytest.mark.parametrize('hand1,hand2,expected', [
    ('2H 3D 5S 9C KD',  '2C 3H 4S 8C AH', 'Player 2 - High Card'),
    ('2H 4S 4C 2D 4H',  '2S 8S AS QS 3S', 'Player 1 - Full House'),
    ('2H 3D 5S 9C KD',  '2C 3H 4S 8C KH', 'Player 1 - High Card'),
    ('2H 3D 5S 9C KD', '2D 3H 5C 9S KH', 'Tie')
    ('2S 3C 3S 9C 9S', '2S 3C 3S TD TH', 'Player 2 - Two Pairs')

    ])
def test_play(hand1, hand2, expected):
    assert play(Hand(hand1), Hand(hand2)) == expected
