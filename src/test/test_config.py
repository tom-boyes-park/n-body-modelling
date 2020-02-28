from typing import List

import pytest

from config import DefaultConditions
from loaders import Body


@pytest.mark.parametrize(
    ids=[c.name for c in DefaultConditions],
    argnames="conditions",
    argvalues=[c.value for c in DefaultConditions],
)
def test_default_conditions(conditions: List[Body]):
    assert type(conditions) == list
    for body in conditions:
        assert type(body) == Body
