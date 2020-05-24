from argparse import Namespace
from typing import Type

import pytest

from src.setup import validate_args
from tests.utils import null_context


@pytest.mark.parametrize(
    argnames=["args", "expected_exc", "expected_msg"],
    argvalues=[
        (
            Namespace(animate=False, list_orbits=False, orbit=None),
            ValueError,
            "Parameters missing, use -h or --help for options",
        ),
        (
            Namespace(animate=True, list_orbits=False, orbit=None),
            ValueError,
            "--orbit must be supplied in order to animate",
        ),
        (
            Namespace(animate=False, list_orbits=False, orbit="invalid orbit"),
            ValueError,
            "Orbit 'invalid orbit' not recognised",
        ),
        (
            Namespace(animate=True, list_orbits=False, orbit="another invalid orbit"),
            ValueError,
            "Orbit 'another invalid orbit' not recognised",
        ),
        (Namespace(animate=False, list_orbits=False, orbit="BROUCKE_A_2"), None, None,),
        (Namespace(animate=True, list_orbits=False, orbit="BROUCKE_A_2"), None, None,),
        (Namespace(animate=False, list_orbits=True, orbit=None), None, None,),
        (
            Namespace(animate=True, list_orbits=True, orbit="BROUCKE_A_2"),
            None,
            None,
        ),  # whilst this doesn't make complete sense as arguments, it's technically
        # valid. Valid orbits will be logged to console and application will exit
    ],
)
def test_validate_orbit(
    args: Namespace, expected_exc: Type[Exception], expected_msg: str
):
    with pytest.raises(
        expected_exc, match=expected_msg
    ) if expected_exc else null_context():
        validate_args(args)
