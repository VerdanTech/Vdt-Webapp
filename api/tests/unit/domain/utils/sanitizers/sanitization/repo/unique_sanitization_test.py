from typing import Any, List

import pytest
from litestar.contrib.repository.testing.generic_mock_repository import (
    GenericAsyncMockRepository,
)
from src.verdantech_api.domain.models.common.entities import MockEntity
from src.verdantech_api.domain.utils.sanitizers.sanitization.repo.unique import (
    UniqueSanitization,
    UniqueSanitizationConfig,
    UniqueSanitizationSpec,
)


class TestUniqueSanitization:
    @pytest.mark.parametrize(
        ["input", "spec", "existing_entities", "expected_output"],
        [
            # Test case: input field not found
            (
                0,
                UniqueSanitizationSpec(field="int_field"),
                [MockEntity(int_field=1, str_field="")],
                True,
            ),
            # Test case: input field found
            (
                0,
                UniqueSanitizationSpec(field="int_field"),
                [MockEntity(int_field=0, str_field="")],
                False,
            ),
        ],
    )
    async def test_unique_base_sanitization(
        self,
        input: Any,
        spec: UniqueSanitizationSpec,
        existing_entities: List[MockEntity],
        expected_output: bool,
        mock_entity_repo: GenericAsyncMockRepository,
    ):
        """Ensure the uniquness validation works as expected

        Args:
            input (Any): the input to test validation on
            spec (UniqueSanitizationSpec): the field to
                validate uniqueness on
            existing_entities (List[MockEntity]): a list of
                entities to mock existing persistence
            expected_output (bool): expected validation result
            test_repo (GenericAsyncMockRepository): fixture providing
                mock repository configured to accept MockEntitiy
        """
        await mock_entity_repo.add_many(existing_entities)
        sanitization = UniqueSanitization(
            UniqueSanitizationConfig(spec=spec, repo=mock_entity_repo, error_message="")
        )
        assert await sanitization._base_sanitization(input=input) == expected_output
