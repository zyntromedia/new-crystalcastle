"""
Pytest shared fixtures — v1.9.0-TESTED
"""
import pytest
from httpx import AsyncClient
from main import app


@pytest.fixture(scope="function")
async def client():
    """Test client — created fresh for each test"""
    async with AsyncClient(app=app, base_url="http://test") as ac:
        yield ac


@pytest.fixture(scope="session")
def anyio_backend():
    """Specify async backend for pytest-asyncio"""
    return "asyncio"
