# External Libraries
import pytest
from pytest_mock import MockerFixture

# VerdanTech Source
from src.utils.sanitizers import options
from src.utils.sanitizers.field import FieldSanitizer
from src.utils.sanitizers.object import ObjectSanitizer, ObjectSanitizerConfig
from src.utils.sanitizers.spec import SpecError

pytestmark = [pytest.mark.unit]


class TestObjectSanitizer:
    # ======================================
    # ObjectSanitizer.sanitize() tests
    # ======================================

    async def test_sanitize_error_raised(self, mocker: MockerFixture) -> None:
        """
        Ensure that if _sanitize returns an error, it is raise as a SpecError.

        Args:
            mocker (MockerFixture): pytest-mock.
        """
        input_data = {"field1": "sanitized_data"}
        error_dict = {"field1": {"Spec": "Spec validation failed"}}

        mock_field_sanitizer = mocker.MagicMock(spec=FieldSanitizer)
        config = ObjectSanitizerConfig(field1=mock_field_sanitizer)
        object_sanitizer = ObjectSanitizer(config=config)

        mocker.patch.object(
            object_sanitizer, "_sanitize", return_value=(input_data, error_dict)
        )

        with pytest.raises(SpecError) as error:
            await object_sanitizer.sanitize(
                input_data=input_data,
                spec_select={"field1": [options.SelectEnum.ENABLE_ALL]},
            )

        assert error.value.args[0] == error_dict

    async def test_sanitize(self, mocker: MockerFixture) -> None:
        """
        Ensure that if _sanitize returns no error, the sanitized data
        is returned.

        Args:
            mocker (MockerFixture): pytest-mock.
        """
        input_data = {"field1": "sanitized_data"}
        error_dict = {}

        mock_field_sanitizer = mocker.MagicMock(spec=FieldSanitizer)
        config = ObjectSanitizerConfig(field1=mock_field_sanitizer)
        object_sanitizer = ObjectSanitizer(config=config)

        mocker.patch.object(
            object_sanitizer, "_sanitize", return_value=(input_data, error_dict)
        )

        expected_output_data = input_data

        sanitized_data = await object_sanitizer.sanitize(
            input_data=input_data,
            spec_select={"field1": [options.SelectEnum.ENABLE_ALL]},
        )

        assert sanitized_data == expected_output_data

    # ======================================
    # ObjectSanitizer._sanitize() tests
    # ======================================

    async def test__sanitize_no_field_sanitizer_for_field_raises_value_error(
        self, mocker: MockerFixture
    ) -> None:
        """
        Ensure that if the object sanitizer is called with an input field
        for which it has no FieldSanitizer, a ValueError is raised.

        Args:
            mocker (MockerFixture): pytest-mock.
        """
        mock_field_sanitizer = mocker.MagicMock(spec=FieldSanitizer)
        config = ObjectSanitizerConfig(field1=mock_field_sanitizer)
        object_sanitizer = ObjectSanitizer(config=config)

        with pytest.raises(ValueError):
            await object_sanitizer._sanitize(
                input_data={"field_does_not_exist": "input_data"},
                spec_select={"field1": [options.SelectEnum.ENABLE_ALL]},
            )

    async def test__sanitize(self, mocker: MockerFixture) -> None:
        """
        Ensure all FieldSanitizers on ObjectSanitizer are called and both
        their normalized data and error dicts are used to construct the
        return error dict.

        Args:
            mocker (MockerFixture): pytest-mock.
        """
        input_data = {"field1": "input_data1", "field2": "input_data2"}

        # Mock two FieldSanitizer - 1 returns normalized data, 2 returns an error
        mock_field_sanitizer1 = mocker.MagicMock(spec=FieldSanitizer)
        mock_field_sanitizer2 = mocker.MagicMock(spec=FieldSanitizer)
        mock_field_sanitizer1.sanitize.return_value = ("input_data1_normalized", {})
        mock_field_sanitizer2.sanitize.return_value = (
            "input_data2",
            {"Spec": "Spec validation failed"},
        )

        # The expected output is the normalized data and error
        expected_output_data = {
            "field1": "input_data1_normalized",
            "field2": "input_data2",
        }
        expected_error = {"field2": {"Spec": "Spec validation failed"}}

        config = ObjectSanitizerConfig(
            field1=mock_field_sanitizer1, field2=mock_field_sanitizer2
        )
        object_sanitizer = ObjectSanitizer(config=config)

        sanitized_data, error = await object_sanitizer._sanitize(
            input_data=input_data,
            spec_select={
                "field1": [options.SelectEnum.ENABLE_ALL],
                "field2": [options.SelectEnum.ENABLE_ALL],
            },
        )

        assert sanitized_data == expected_output_data
        assert error == expected_error
