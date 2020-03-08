from typing import List

import pytest

from src.config import Body, DefaultConditions


@pytest.mark.parametrize(
    ids=[c.name for c in DefaultConditions],
    argnames="conditions",
    argvalues=[c.value for c in DefaultConditions],
)
def test_default_conditions_are_lists(conditions: List[Body]):
    assert isinstance(conditions, list)


@pytest.mark.parametrize(
    ids=[c.name for c in DefaultConditions],
    argnames="conditions",
    argvalues=[c.value for c in DefaultConditions],
)
def test_default_conditions_are_lists_of_bodies(conditions: List[Body]):
    for body in conditions:
        assert isinstance(body, Body)
