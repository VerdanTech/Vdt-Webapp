from contextlib import nullcontext

import pytest


@pytest.fixture
def error_context(request):
    if request.param is None:
        return nullcontext()
    else:
        return pytest.raises(request.param)
