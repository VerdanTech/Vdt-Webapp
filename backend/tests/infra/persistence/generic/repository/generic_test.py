# External Libraries
import pytest
from pytest_mock import MockerFixture

# VerdanTech Source
from mocks.infra.persistence.repository import MockBaseRepository
from src.interfaces.persistence import exceptions


class TestBaseRepository:
    # ======================================
    # BaseRepository.async_dynamic_call() tests
    # ======================================

    @pytest.mark.parametrize(("bypass_validation"), [(False, True)])
    async def test_async_dynamic_call_validation(
        self, bypass_validation: bool, mocker: MockerFixture
    ) -> None:
        """
        Ensure that the validate_async_dynamic_call_signature
        method is called when bypass_validation is False.

        Args:
            bypass_validation (bool): parametrized value of
                bypass_validation.
            mocker (MockerFixture): pytest-mock
        """
        repo = MockBaseRepository()

        async def mock_method():
            pass

        setattr(repo, "mock_method", mock_method)

        mock_validate_async_dynamic_call_signature = mocker.patch.object(
            repo, "validate_async_dynamic_call_signature"
        )

        await repo.async_dynamic_call(
            "mock_method", bypass_validation=bypass_validation
        )

        if bypass_validation:
            mock_validate_async_dynamic_call_signature.assert_not_called()
        else:
            mock_validate_async_dynamic_call_signature.assert_called_once()

    async def test_async_dynamic_call_success(self) -> None:
        """
        Ensure that the repository's method is successfully called
        with the supplied keyword arguments.
        """
        repo = MockBaseRepository()

        async def mock_method(arg1: str, arg2: str) -> int:
            return arg1 + arg2

        arg1 = "abc"
        arg2 = "def"
        expected_output = "abcdef"

        setattr(repo, "mock_method", mock_method)

        output = await repo.async_dynamic_call(
            "mock_method", bypass_validation=True, arg1=arg1, arg2=arg2
        )

        assert output == expected_output

    # ======================================
    # BaseRepository.validate_async_dynamic_call_signature() tests
    # ======================================

    async def test_validate_async_dynamic_call_signature_invalid_method_none(
        self,
    ) -> None:
        """
        Ensure that when no attribute matching the method_name exists on the
        repository, an InterfaceReporitoryError is raised.
        """
        repo = MockBaseRepository()

        with pytest.raises(exceptions.InterfaceRepositoryError):
            repo.validate_async_dynamic_call_signature("non_existant_method")

    async def test_validate_async_dynamic_call_signature_invalid_method_non_awaitable(
        self,
    ) -> None:
        """
        Ensure that when the existing attribute matching method_name exists on
        the repository but is not an async method, an InterfaceRepositoryError is raised.
        """
        repo = MockBaseRepository()

        def non_awaitable_method():
            pass

        setattr(repo, "non_awaitable_method", non_awaitable_method)

        with pytest.raises(exceptions.InterfaceRepositoryError):
            repo.validate_async_dynamic_call_signature("non_awaitable_method")

    async def test_validate_async_dynamic_call_signature_unmatched_kwargs(self) -> None:
        """
        Ensure that when the async method matching method_name does not contain parameters
        matching all the keyword arguments specified, an InterfaceRepositoryError is raised.
        """
        repo = MockBaseRepository()

        async def awaitable_method(arg1):
            pass

        setattr(repo, "awaitable_method", awaitable_method)

        with pytest.raises(exceptions.InterfaceRepositoryError):
            repo.validate_async_dynamic_call_signature(
                "awaitable_method", arg1="", arg2=""
            )

    async def test_validate_async_dynamic_call_signature_unmatched_parameters(
        self,
    ) -> None:
        """
        Ensure that when the async method matching method_name contains parameters
        that are unmatched by the keyword arguments specified, an InterfaceRepositoryError is raised.
        """
        repo = MockBaseRepository()

        async def awaitable_method(arg1):
            pass

        setattr(repo, "awaitable_method", awaitable_method)

        with pytest.raises(exceptions.InterfaceRepositoryError):
            repo.validate_async_dynamic_call_signature(
                "awaitable_method", arg1="", arg2=""
            )

    async def test_validate_async_dynamic_call_signature_success(self) -> None:
        """
        Ensure that when the async method matching method_name exists on the
        repository and accepts parameters that match with the specified keyword_arguments,
        the function returns without raising an error.
        """
        repo = MockBaseRepository()

        async def awaitable_method(arg1, arg2):
            pass

        setattr(repo, "awaitable_method", awaitable_method)

        repo.validate_async_dynamic_call_signature(
            "awaitable_method", arg1="arg1", arg2="arg2"
        )
