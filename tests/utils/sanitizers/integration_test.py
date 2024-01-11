# External Libraries
import pytest

# VerdanTech Source
from src.utils.sanitizers import options
from src.utils.sanitizers.basic import ban, length
from src.utils.sanitizers.field import FieldSanitizer
from src.utils.sanitizers.object import ObjectSanitizer, ObjectSanitizerConfig
from src.utils.sanitizers.spec import SpecError

pytestmark = [pytest.mark.unit]


async def test_multi_field_multi_spec_object_sanitizer() -> None:
    """
    Ensure that when a full ObjectSanitizer with multiple FieldSanitizers and Specs
    is constructed, that the correct Specs are run based on spec_select, and the
    error messages are combined and formatted with the Spec params and input data.
    """
    object_sanitizer = ObjectSanitizer(
        config=ObjectSanitizerConfig(
            field1=FieldSanitizer(
                [
                    length.LengthSpec(
                        config=length.LengthSpecConfig(
                            params=length.LengthSpecParams(min=0, max=50),
                            error_message="Field 1 length spec error message {max}, {min}, {input_data}",
                        )
                    ),
                    ban.BanSpec(
                        config=ban.BanSpecConfig(
                            params=ban.BanSpecParams(banned_inputs=["banned_input1"]),
                            error_message="Field 1 ban spec error_message {banned_inputs}, {input_data}",
                            case_sensitive=False,
                        )
                    ),
                ]
            ),
            field2=FieldSanitizer(
                [
                    length.LengthSpec(
                        config=length.LengthSpecConfig(
                            params=length.LengthSpecParams(min=0, max=2),
                            error_message="Field 2 length spec error message {max}, {min}, {input_data}",
                        )
                    ),
                    ban.BanSpec(
                        config=ban.BanSpecConfig(
                            params=ban.BanSpecParams(
                                banned_inputs=["over_length_spec_and_banned"]
                            ),
                            error_message="Field 2 ban spec error_message {banned_inputs}, {input_data}",
                            case_sensitive=False,
                        )
                    ),
                ]
            ),
            field3=FieldSanitizer(
                [
                    length.LengthSpec(
                        config=length.LengthSpecConfig(
                            params=length.LengthSpecParams(min=0, max=5),
                            error_message="Field 3 length spec error message {max}, {min}, {input_data}",
                        )
                    ),
                    ban.BanSpec(
                        config=ban.BanSpecConfig(
                            params=ban.BanSpecParams(
                                banned_inputs=[
                                    "over_length_spec_and_banned_but_banned_spec_is_not_enabled"
                                ]
                            ),
                            error_message="Field 3 ban spec error_message {banned_inputs}, {input_data}",
                            case_sensitive=False,
                        )
                    ),
                ]
            ),
        )
    )

    input_data = {
        "field1": "within_length_spec_and_not_banned",
        "field2": "over_length_spec_and_banned",
        "field3": "over_length_spec_and_banned_but_banned_spec_is_not_enabled",
    }
    spec_select = {
        "field1": [options.SelectEnum.ENABLE_ALL],
        "field2": [options.SelectEnum.ENABLE_ALL],
        "field3": [options.SelectEnum.LENGTH],
    }
    expected_error = {
        "field2": {
            "LengthSpec": "Field 2 length spec error message 2, 0, over_length_spec_and_banned",
            "BanSpec": "Field 2 ban spec error_message ['over_length_spec_and_banned'], over_length_spec_and_banned",
        },
        "field3": {
            "LengthSpec": "Field 3 length spec error message 5, 0, over_length_spec_and_banned_but_banned_spec_is_not_enabled"
        },
    }

    with pytest.raises(SpecError) as error:
        await object_sanitizer.sanitize(input_data=input_data, spec_select=spec_select)

    assert error.value.args[0] == expected_error
