import pytest

from framework.common.client import ApiClient
from framework.resources import Resources


@pytest.fixture(name="resources", scope="session")
def fixture_platform_with_session():
    """
    Initialises a Resources object that represents all the APIs under test
    """
    api_client = ApiClient()
    resources = Resources(api_client=api_client)
    yield resources


@pytest.fixture
def charging_reset(resources):
    """
    Switch state from A to B, and then teardown to A
    """
    resources.ev.charging.put("reset")
    yield
    resources.ev.charging.put("reset")


@pytest.fixture
def charging_connect(resources):
    resources.ev.charging.put("connect")
    yield


@pytest.fixture
def charging_disconnect(resources):
    resources.ev.charging.put("disconnect")
    yield


@pytest.fixture
def charging_start(resources):
    resources.ev.charging.put("start")
    yield


@pytest.fixture
def charging_stop(resources):
    resources.ev.charging.put("stop")
    yield


@pytest.fixture
def charging_error(resources):
    resources.ev.charging.put("error")
    yield
