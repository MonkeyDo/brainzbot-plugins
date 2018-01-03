import pytest
from brainzbot_plugins.base import DummyApp
from brainzbot_plugins.plugins import bangmotivate


@pytest.fixture
def app():
    return DummyApp(test_plugin=bangmotivate.Plugin())


def test_motivate(app):
    responses = app.respond("!m BrainzBot")
    assert responses == ["You're doing good work, BrainzBot!"]


def test_nomotivate(app):
    responses = app.respond("shouldn't !m === false?")
    assert len(responses) == 0
