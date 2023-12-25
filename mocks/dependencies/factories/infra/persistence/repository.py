# VerdanTech Source
from mocks.infra.persistence.repository.user_mock import MockUserRepository

# ============================================================================
# PROVIDER METHODS
# ============================================================================


async def provide_user_mock_repository() -> MockUserRepository:
    """Configure and provide a mock user repository for testing."""
    return MockUserRepository()
