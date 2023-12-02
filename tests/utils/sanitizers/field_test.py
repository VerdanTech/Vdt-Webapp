# Standard Library
from typing import ContextManager, List

# External Libraries
import pytest
from pytest_mock import MockerFixture

# VerdanTech Source
from src.utils.sanitizers import basic
from src.utils.sanitizers.field import FieldSanitizer
from src.utils.sanitizers.options import GroupErrorsByEnum, SelectEnum
from src.utils.sanitizers.spec import Spec, SpecError

pytestmark = [pytest.mark.unit]


class TestFieldSanitizer:
    # ======================================
    # FieldSanitizer.__init__() tests
    # ======================================

    def test___init__(self, length_regex_ban_specs_fixture: List[Spec]) -> None:
        """
        Ensure that the Specs passed in as arguments are set
        on the specs attribute on the FieldSanitizer, and a reference
        to the FieldSanitizer is set on each Spec.

        Args:
            length_regex_ban_specs_fixture (List[Spec]): fixture providing
                list of length, regex, and ban Specs.
        """

        field_sanitizer = FieldSanitizer[
            basic.length.LengthSpec, basic.regex.RegexSpec, basic.ban.BanSpec
        ](*length_regex_ban_specs_fixture)

        for spec in length_regex_ban_specs_fixture:
            assert any(
                spec.id == field_sanitizer_spec.id
                for field_sanitizer_spec in field_sanitizer.specs
            )
            assert spec.field == field_sanitizer

    # ======================================
    # FieldSanitizer.sanitize() tests
    # ======================================

    async def test_sanitize_error_group_errors_by_object(
        self, length_regex_ban_specs_fixture: List[Spec], mocker: MockerFixture
    ) -> None:
        """
        Ensure that the error message returned by _sanitize is returned if
        group_errors_by is OBJECT.

        Args:
            length_regex_ban_specs_fixture (List[Spec]): fixture providing
                list of length, regex, and ban Specs.
            mocker (MockerFixture): pytest-mock.
        """
        _sanitize_output_error_message = {
            "LengthSpec": "error_message1",
            "RegexSpec": "error_message2",
            "BanSpec": "error_message3",
        }

        field_sanitizer = FieldSanitizer[
            basic.length.LengthSpec, basic.regex.RegexSpec, basic.ban.BanSpec
        ](*length_regex_ban_specs_fixture)

        mocker.patch.object(
            field_sanitizer, "_sanitize", return_value=_sanitize_output_error_message
        )

        input_data = "input_data"
        expected_output = (input_data, _sanitize_output_error_message)

        output = await field_sanitizer.sanitize(
            input_data=input_data,
            spec_select=[],
            group_errors_by=GroupErrorsByEnum.OBJECT,
        )

        assert output == expected_output

    @pytest.mark.parametrize(
        ("group_errors_by"),
        [
            (GroupErrorsByEnum.FIELD),
            (GroupErrorsByEnum.SPEC),
        ],
    )
    async def test_sanitize_error_group_errors_by_field_or_spec(
        self,
        group_errors_by: GroupErrorsByEnum,
        length_regex_ban_specs_fixture: List[Spec],
        mocker: MockerFixture,
    ) -> None:
        """
        Ensure that the error message returned by _sanitize is raised if
        group_errors_by is FIELD or SPEC.

        Args:
            group_errors_by (GroupErrorsByEnum): parametrized value of
                group_errors_by argument
            length_regex_ban_specs_fixture (List[Spec]): fixture providing
                list of length, regex, and ban Specs.
            mocker (MockerFixture): pytest-mock.
        """
        _sanitize_output_error_message = {
            "LengthSpec": "error_message1",
            "RegexSpec": "error_message2",
            "BanSpec": "error_message3",
        }

        field_sanitizer = FieldSanitizer[
            basic.length.LengthSpec, basic.regex.RegexSpec, basic.ban.BanSpec
        ](*length_regex_ban_specs_fixture)

        mocker.patch.object(
            field_sanitizer, "_sanitize", return_value=_sanitize_output_error_message
        )

        input_data = "input_data"
        expected_output_error_message = _sanitize_output_error_message

        with pytest.raises(SpecError) as error:
            await field_sanitizer.sanitize(
                input_data=input_data,
                spec_select=[],
                group_errors_by=group_errors_by,
            )

        assert error.value.args[0] == expected_output_error_message

    # ======================================
    # FieldSanitizer._sanitize() tests
    # ======================================

    async def test__sanitize(
        self, length_regex_ban_specs_fixture: List[Spec], mocker: MockerFixture
    ) -> None:
        """
        Ensure that all the Specs returned by _select_specs have their
        error messages collected and added to the output.

        Args:
            length_regex_ban_specs_fixture (List[Spec]): fixture providing
                list of length, regex, and ban Specs.
            mocker (MockerFixture): pytest-mock
        """
        mocker.patch.object(
            length_regex_ban_specs_fixture[0], "sanitize", return_value="error_message1"
        )
        mocker.patch.object(
            length_regex_ban_specs_fixture[1], "sanitize", return_value="error_message2"
        )
        mocker.patch.object(
            length_regex_ban_specs_fixture[2], "sanitize", return_value="error_message3"
        )

        field_sanitizer = FieldSanitizer[
            basic.length.LengthSpec, basic.regex.RegexSpec, basic.ban.BanSpec
        ](*length_regex_ban_specs_fixture)

        mocker.patch.object(
            field_sanitizer, "_select_specs", return_value=field_sanitizer.specs
        )

        input_data = "input_data"
        spec_select = []
        expected_output = {
            "LengthSpec": "error_message1",
            "RegexSpec": "error_message2",
            "BanSpec": "error_message3",
        }

        output = await field_sanitizer._sanitize(
            input_data=input_data, spec_select=spec_select
        )

        assert output == expected_output

    # ======================================
    # FieldSanitizer._select_specs() tests
    # ======================================

    @pytest.mark.parametrize(
        ("spec_select", "apply_default", "expected_output"),
        [
            # Test case: spec_select is ENABLE_ALL, then the output
            # contains all specs regardless of apply_default
            (
                [SelectEnum.ENABLE_ALL],
                False,
                [SelectEnum.LENGTH, SelectEnum.REGEX, SelectEnum.BAN],
            ),
            # Test case: spec_select is ENABLE_ALL, then the output
            # contains all specs regardless of apply_default
            (
                [SelectEnum.ENABLE_ALL],
                True,
                [SelectEnum.LENGTH, SelectEnum.REGEX, SelectEnum.BAN],
            ),
            # Test case: spec_select is DISABLE_ALL, then the output
            # contains no specs regardless of apply_default
            (
                [SelectEnum.DISABLE_ALL],
                False,
                [],
            ),
            # Test case: spec_select is DISABLE_ALL, then the output
            # contains no specs regardless of apply_default
            (
                [SelectEnum.DISABLE_ALL],
                True,
                [],
            ),
            # Test case: spec_select contains a list of Spec IDs,
            # and apply_default is False, then the output contains
            # only the specs with IDs in spec_select
            ([SelectEnum.LENGTH], False, [SelectEnum.LENGTH]),
            # Test case: spec_select contains a list of Spec IDs,
            # and apply_default is True, then the output contains
            # only the specs with IDs not in spec_select
            ([SelectEnum.LENGTH], True, [SelectEnum.REGEX, SelectEnum.BAN]),
        ],
    )
    async def test__select_specs(
        self,
        spec_select: List[SelectEnum],
        apply_default: bool,
        expected_output: List[SelectEnum],
        length_regex_ban_specs_fixture: List[Spec],
    ) -> None:
        """
        Ensure that the spec_select and apply_default arguments
        are correctly used to select the FieldSanitizer's specs attribute

        Args:
            spec_select (List[SelectEnum]): the value of spec_select
                to test
            apply_default (bool): the value of apply_default to test
            expected_output (List[SelectEnum]): the expected output to assert
            length_regex_ban_specs_fixture (List[Spec]): fixture providing
                list of length, regex, and ban Specs.
        """
        field_sanitizer = FieldSanitizer(*length_regex_ban_specs_fixture)

        output = field_sanitizer._select_specs(
            spec_select=spec_select, apply_default=apply_default
        )

        for spec in output:
            assert spec.id in expected_output
