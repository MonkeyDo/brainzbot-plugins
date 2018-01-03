import pytest
from brainzbot_plugins.base import DummyApp
from brainzbot_plugins.plugins import ping

@pytest.fixture
def app():
    app_instance = DummyApp(test_plugin=ping.Plugin())
    return app_instance


def test_ping(app):
    responses = app.respond("@ping")
    assert responses == ["Are you in need of my services, repl_user?"]


def test_noping(app):
    responses = app.respond("shouldn't ping === false?")
    assert len(responses) == 0
