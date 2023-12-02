# External Libraries
import pytest

# VerdanTech Source
from src.utils.sanitizers.basic.ban import BanSpec, BanSpecConfig, BanSpecParams

pytestmark = [pytest.mark.unit]


class TestBanSpec:
    # ======================================
    # BanSpec._sanitize() tests
    # ======================================

    @pytest.mark.parametrize(
        [
            "input_data",
            "params",
            "case_sensitive",
            "expected_output",
        ],
        [
            # Test case: float not in banned_inputs returns true
            (0.5, BanSpecParams(banned_inputs=[0.1, 0.2, 0.3]), False, True),
            # Test case: float in banned_inputs returns false
            (0.5, BanSpecParams(banned_inputs=[0.1, 0.2, 0.5]), False, False),
            # Test case: str not in banned_inputs returns true
            ("str", BanSpecParams(banned_inputs=["str1", "str2"]), False, True),
            # Test case: str in banned_inputs returns false
            ("str", BanSpecParams(banned_inputs=["str1", "str"]), False, False),
            # Test case: str in banned_inputs
            # with case_sensitive = True
            # returns True
            ("sTr", BanSpecParams(banned_inputs=["str"]), True, True),
            # Test case: str in normalized(banned_inputs)
            # with case_sensitive = False
            # returns false
            ("sTr", BanSpecParams(banned_inputs=["str"]), False, False),
        ],
    )
    def test_ban_spec_minimum_bound(
        self,
        input_data: str,
        params: BanSpecParams,
        case_sensitive: bool,
        expected_output: bool,
    ):
        """
        Ensure the inner sanitization logic rejects inputs with lengths
        greater than params.min.

        Args:
            input_data (Real): the input to test validation on.
            params (LengthSpecParams): the min and max values
                to use for validation.
            case_sensitive (bool): the value of BanSpecConfig.case_sensitive
                to set on the BanSpec under test.
            expected_output (bool): the expected result of the validation.
        """
        config = BanSpecConfig(
            params=params, error_message="", case_sensitive=case_sensitive
        )
        spec = BanSpec(config=config)
        assert spec._sanitize(input_data=input_data) == expected_output
