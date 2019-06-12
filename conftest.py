import pytest
from fixture.hw_application import Application
from fixture.contact_application import Application


@pytest.fixture(scope="session")
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

