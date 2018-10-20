#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
import json

from poker.hand import Hand
from poker.exceptions import DuplicatedCardError


def get_ranks(rank):
    with open('tests/ranks.json') as f:
        data = json.load(f)
    return [(k, v) for k, v in data.items() if v == rank]


@pytest.mark.parametrize('hand', [
    '2D 2S 4Q 4K 4K',
    '2D 2S 4Q 6K 4Q',
    ])
def test_invalid_hand(hand):
    with pytest.raises(DuplicatedCardError):
        Hand(hand)


@pytest.mark.parametrize('hand, expected', get_ranks('High Card'))
def test_rank_high_card(hand, expected):
    assert Hand(hand).rank() == expected


@pytest.mark.parametrize('hand, expected', get_ranks('Pair'))
def test_rank_pair(hand, expected):
    assert Hand(hand).rank() == expected


@pytest.mark.parametrize('hand, expected', get_ranks('Two Pairs'))
def test_rank_two_pairs(hand, expected):
    assert Hand(hand).rank() == expected


@pytest.mark.parametrize('hand, expected', get_ranks('Three of a Kind'))
def test_rank_three_of_a_kind(hand, expected):
    assert Hand(hand).rank() == expected


@pytest.mark.parametrize('hand, expected', get_ranks('Straight'))
def test_rank_staight(hand, expected):
    assert Hand(hand).rank() == expected


@pytest.mark.parametrize('hand, expected', get_ranks('Flush'))
def test_rank_flush(hand, expected):
    assert Hand(hand).rank() == expected


@pytest.mark.parametrize('hand, expected', get_ranks('Four of a Kind'))
def test_rank_four_of_a_kind(hand, expected):
    assert Hand(hand).rank() == expected


@pytest.mark.parametrize('hand, expected', get_ranks('Straight Flush'))
def test_rank_straight_flush(hand, expected):
    assert Hand(hand).rank() == expected
