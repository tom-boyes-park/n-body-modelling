from argparse import Namespace
from typing import Type

import pytest

from src.config import Orbit, YING_YANG_2B, TWO_LIGHT_ONE_MASSIVE
from src.main import parse_and_validate_args


@pytest.mark.parametrize(
    argnames=["args", "expected_exc", "expected_msg", "expected_orbit"],
    argvalues=[
        (Namespace(list_orbits=True, orbit=None), SystemExit, None, None),
        (Namespace(list_orbits=True, orbit="some orbit"), SystemExit, None, None),
        (
            Namespace(list_orbits=False, orbit=None),
            ValueError,
            "Orbit name must be specified",
            None,
        ),
        (
            Namespace(list_orbits=False, orbit="some orbit"),
            ValueError,
            "'some orbit' not recognised",
            None,
        ),
    ],
)
def test_parse_and_validate_args_raises(
    args: Namespace,
    expected_exc: Type[BaseException],
    expected_msg: str,
    expected_orbit,
):

    with pytest.raises(expected_exc) as exc_info:
        orbit = parse_and_validate_args(args=args)
        assert exc_info.value.args[0] == expected_msg
        assert orbit == expected_orbit


@pytest.mark.parametrize(
    argnames=["args", "expected_orbit"],
    argvalues=[
        (Namespace(list_orbits=False, orbit="YING_YANG_2B"), YING_YANG_2B),
        (
            Namespace(list_orbits=False, orbit="TWO_LIGHT_ONE_MASSIVE"),
            TWO_LIGHT_ONE_MASSIVE,
        ),
    ],
)
def test_parse_and_validate_args(args: Namespace, expected_orbit: Orbit):
    orbit = parse_and_validate_args(args=args)
    assert orbit == expected_orbit
