# Standard Library
import re
from typing import List

# External Libraries
import pytest

# VerdanTech Source
from src.utils.sanitizers import basic
from src.utils.sanitizers.spec import Spec


@pytest.fixture
def length_regex_ban_specs_fixture() -> List[Spec]:
    return [
        basic.length.LengthSpec(
            config=basic.length.LengthSpecConfig(
                params=basic.length.LengthSpecParams(min=0, max=10), error_message=""
            )
        ),
        basic.regex.RegexSpec(
            config=basic.regex.RegexSpecConfig(
                params=basic.regex.RegexSpecParams(pattern=re.compile("")),
                error_message="",
            )
        ),
        basic.ban.BanSpec(
            config=basic.ban.BanSpecConfig(
                params=basic.ban.BanSpecParams(banned_inputs=["banned_input1"]),
                error_message="",
                case_sensitive=False,
            )
        ),
    ]
