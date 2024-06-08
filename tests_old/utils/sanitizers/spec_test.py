# Standard Library
from typing import Any, Dict

# External Libraries
import pytest
from pytest_mock import MockerFixture

# VerdanTech Source
from src.utils.sanitizers import options
from src.utils.sanitizers.spec import Spec, SpecConfig, SpecError, SpecParams

pytestmark = [pytest.mark.unit]


class TestSpecConfig:
    # ======================================
    # SpecConfig.validate_error_message_params() tests
    # ======================================

    @pytest.mark.parametrize(
        ("error_message", "params"),
        [
            # Test case: there are parameter placeholders in the error
            # string that are not satisfied by any parameters in the config.
            ("--{param1} {param2}--", {"param1": None}),
        ],
    )
    def test___post_init___raises_value_error_with_invalid_params(
        self,
        error_message: str,
        params: Dict[str, Any],
    ) -> None:
        """
        Ensure that all test cases raise a ValueError.

        Args:
            error_message (str): error message to configure.
            params (Dict[str, Any]): parameters to configure.
        """
        with pytest.raises(ValueError):
            SpecConfig(params=params, error_message=error_message)

    @pytest.mark.parametrize(
        ("error_message", "params"),
        [
            # Test case: all parameter placeholders in the
            # error string are satisfied by parameters in the config.
            ("--{param1} {param2}--", {"param1": None, "param2": None}),
            # Test case: all parameter placeholders in the
            # error string are satisfied by parameters in the config
            # and there are parameters in the config that don't have
            # matching placeholders in the error_message.
            ("--{param1}--", {"param1": None, "param2": None}),
            # Test case: no placeholders, and params is None.
            ("", None),
        ],
    )
    def test___post_init___success(
        self,
        error_message: str,
        params: Dict[str, Any],
    ) -> None:
        """
        Ensure that no error is raised in any of the test cases.

        Args:
            error_message (str): error message to configure.
            params (Dict[str, Any]): parameters to configure.
        """
        SpecConfig(params=params, error_message=error_message)


class TestSpec:
    # ======================================
    # Spec.sanitize() tests
    # ======================================

    async def test_sanitize_true_validation(
        self,
        mocker: MockerFixture,
    ) -> None:
        """
        Ensure that when the result of the inner
        sanitization function (_sanitize) is True,
        the output of the outer sanitize function (sanitize)
        is None

        Args:
            mocker (MockerFixture): pytest-mock
        """
        input_data = 10
        sanitization_result = True

        params = SpecParams()
        params["param1"] = "param1"
        params["param2"] = 22
        error_message = ""

        config = SpecConfig(params=params, error_message=error_message)
        spec = Spec(config=config)

        _sanitize_mock = mocker.patch.object(
            spec,
            "_sanitize",
            return_value=sanitization_result,
        )

        error = await spec.sanitize(input_data=input_data)
        assert error is None
        _sanitize_mock.assert_called_once_with(input_data=input_data)

    @pytest.mark.parametrize(
        ("group_errors_by"),
        [(options.GroupErrorsByEnum.FIELD), (options.GroupErrorsByEnum.OBJECT)],
    )
    async def test_sanitize_false_validation_group_errors_field_or_group(
        self,
        group_errors_by: options.GroupErrorsByEnum,
        mocker: MockerFixture,
    ) -> None:
        """
        Ensure that when the result of the inner
        santitization function (_sanitize) is False
        and the group_errors_by option is FIELD or GROUP,
        the error message is returned with the params and
        input_data formatted into the error message.

        Args:
            group_errors_by (GroupErrorsByEnum): parameter.
            mocker (MockerFixture): pytest-mock.
        """
        input_data = 10
        sanitization_result = False

        params = SpecParams()
        params["param1"] = "param1"
        params["param2"] = 22
        params["param3"] = 33

        error_message = """An error message should be formatted 
                            with {param1} and {param2} and {input_data}"""
        error_message_format_parameters = {**params, "input_data": input_data}
        expected_error_message = error_message.format(**error_message_format_parameters)

        config = SpecConfig(params=params, error_message=error_message)
        spec = Spec(config=config)
        _sanitize_mock = mocker.patch.object(
            spec, "_sanitize", return_value=sanitization_result
        )

        error = await spec.sanitize(
            input_data=input_data, group_errors_by=group_errors_by
        )

        assert error == expected_error_message
        _sanitize_mock.assert_called_once_with(input_data=input_data)

    async def test_sanitize_false_validation_group_errors_spec(
        self,
        mocker: MockerFixture,
    ) -> None:
        """
        Ensure that when the result of the inner
        santitization function (_sanitize) is False
        and the group_errors_by option is SPEC,
        the error is raised with the params and
        input_data formatted into the error message.

        Args:
            group_errors_by (GroupErrorsByEnum): parameter.
            mocker (MockerFixture): pytest-mock.
        """
        input_data = 10
        sanitization_result = False
        group_errors_by = options.GroupErrorsByEnum.SPEC

        params = SpecParams()
        params["param1"] = "param1"
        params["param2"] = 22
        params["param3"] = 33

        error_message = """An error message should be formatted 
                            with {param1} and {param2} and {input_data}"""
        error_message_format_parameters = {**params, "input_data": input_data}
        expected_error_message = error_message.format(**error_message_format_parameters)

        config = SpecConfig(params=params, error_message=error_message)
        spec = Spec(config=config)
        _sanitize_mock = mocker.patch.object(
            spec, "_sanitize", return_value=sanitization_result
        )

        return_value = None
        with pytest.raises(SpecError) as error:
            return_value = await spec.sanitize(
                input_data=input_data, group_errors_by=group_errors_by
            )
        assert str(error.value) == expected_error_message
        assert return_value is None
        _sanitize_mock.assert_called_once_with(input_data=input_data)
