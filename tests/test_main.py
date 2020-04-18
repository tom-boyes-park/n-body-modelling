from argparse import Namespace
from typing import Type

import pytest

from src.config import Orbit, YING_YANG_2B, TWO_LIGHT_ONE_MASSIVE
from src.main import validate_args


@pytest.mark.parametrize(
    argnames=["args", "expected_exc", "expected_msg"],
    argvalues=[
        (Namespace(list_orbits=True, orbit=None), SystemExit, None),
        (Namespace(list_orbits=True, orbit="some orbit"), SystemExit, None),
        (
            Namespace(list_orbits=False, orbit=None),
            ValueError,
            "Orbit name must be specified",
        ),
        (
            Namespace(list_orbits=False, orbit="some orbit"),
            ValueError,
            "'some orbit' not recognised",
        ),
    ],
)
def test_parse_and_validate_args_raises(
    args: Namespace,
    expected_exc: Type[BaseException],
    expected_msg: str,
):

    with pytest.raises(expected_exc) as exc_info:
        validate_args(args=args)
        assert exc_info.value.args[0] == expected_msg
