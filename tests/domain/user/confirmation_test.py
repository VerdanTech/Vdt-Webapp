# Standard Library
from datetime import datetime

# External Libraries
import pytest
from pytest_mock import MockerFixture

# VerdanTech Source
from src.domain.user.email import BaseConfirmation

pytestmark = [pytest.mark.unit]



class TestBaseConfirmation:
    # ======================================
    # BaseConfirmation.is_valid() tests
    # ======================================

    @pytest.mark.parametrize(
        ("now", "created_at", "expiry_time_hours", "expected_result"),
        [
            # Test case: outside expiry window, false is returned
            (
                datetime(2023, 9, 16, 12, 0, 0),
                datetime(2023, 9, 16, 10, 0, 0),
                1,
                False,
            ),
            # Test case: inside expiry window, true is returned
            (
                datetime(2023, 9, 16, 12, 0, 0),
                datetime(2023, 9, 16, 11, 0, 0),
                2,
                True,
            ),
        ],
    )
    def test_is_valid(
        self,
        now: datetime,
        created_at: datetime,
        expiry_time_hours: int,
        expected_result: bool,
        mocker: MockerFixture,
    ) -> None:
        """
        Ensure the current time is correctly compared.
        against the time of creation and the expiry length.

        Args:
            now (datetime): mock current datetime.
            created_at (datetime): mock creation datetime.
            expiry_time_hours (int): mock application setting.
            expected_result (bool): expected validation result.
            mocker (MockerFixture): pytest-mock.
        """
        mock_datetime = mocker.patch("src.domain.user.confirmation.datetime")
        mock_datetime.now.return_value = now
        confirmation = BaseConfirmation(key="abc", created_at=created_at)

        assert (
            confirmation.is_valid(expiry_time_hours=expiry_time_hours)
            == expected_result
        )
