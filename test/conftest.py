import pytest

from main.app import create_app
from test.zone_client import ZoneClient


@pytest.fixture()
def app():
    app = create_app()
    app.config.update({
        "TESTING": True,
    })

    yield app


@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture()
def zone_client(client):
    return ZoneClient(client)


@pytest.fixture()
def runner(app):
    return app.test_cli_runner()
