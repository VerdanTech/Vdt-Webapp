# Standard Library

# External Libraries
import pytest
from pytest_mock import MockerFixture

# VerdanTech Source
from src.interfaces.persistence.common import AbstractRepository
from src.utils.sanitizers.repo.unique import UniqueSpec, UniqueSpecConfig

pytestmark = [pytest.mark.unit]


class TestUniqueSpecConfig:
    # ======================================
    # UniqueSpecConfig.__init__() tests
    # ======================================

    def test___init___validates_repo_call_signature(
        self, mocker: MockerFixture
    ) -> None:
        """
        Ensure that the repository's method signature validation is called.
        """
        mock_repo = mocker.MagicMock(spec=AbstractRepository)
        existence_method_name = "existence_method_name"
        existence_method_argument_name = "existence_method_argument_name"

        UniqueSpecConfig(
            error_message="",
            repo=mock_repo,
            existence_method_name=existence_method_name,
            existence_method_argument_name=existence_method_argument_name,
        )

        mock_repo.validate_async_dynamic_call_signature.assert_called_once_with(
            method_name=existence_method_name,
            **{existence_method_argument_name: None},
        )


class TestUniqueSpec:
    # ======================================
    # UniqueSpec._sanitize() tests
    # ======================================

    @pytest.mark.parametrize(
        ("mock_existence_method_return_value", "expected_result"),
        [(True, False), (False, True)],
    )
    async def test_unique_spec(
        self,
        mock_existence_method_return_value: bool,
        expected_result: bool,
        mocker: MockerFixture,
    ):
        """
        Ensure that the unique sanitization logic awaits the async_dynamic_call
        method on the repository, with the proper method name and input_data argument.
        The result of the unique validation is opposite the result of the existence function.

        Args:
            mock_existence_method_return_value (bool): mock return value of the
                repository's existence method, True if the input exists.
            expected_result (bool): the expected result of UniqueSpec._sanitize()
            mocker: (MockerFixture): pytest-mock
        """

        # Config attributes
        existence_method_name = "existence_method_name"
        existence_method_argument_name = "existence_method_argument_name"
        mock_repo = mocker.MagicMock(spec=AbstractRepository)
        mock_repo.async_dynamic_call.return_value = mock_existence_method_return_value

        # Init Spec
        config = UniqueSpecConfig(
            repo=mock_repo,
            existence_method_name=existence_method_name,
            existence_method_argument_name=existence_method_argument_name,
            error_message="",
        )
        spec = UniqueSpec(config=config)

        input_data = "input_data"

        return_value = await spec._sanitize(input_data=input_data)

        assert return_value is expected_result
        mock_repo.async_dynamic_call.assert_awaited_once_with(
            method_name=existence_method_name,
            bypass_validation=True,
            **{existence_method_argument_name: input_data},
        )
