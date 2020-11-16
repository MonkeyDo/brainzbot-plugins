from ..base import BasePlugin
from ..decorators import listens_to_mentions


class Plugin(BasePlugin):
    """
    Simple ping test.

    Curious if I'm still listening? If you say:

        {{ nick }}: ping

    I'll reply to let you know I'm still here.
    """
    @listens_to_mentions(r'^ping$')
    def respond_to_ping(self, line):
        return f'Are you in need of my services, {line.user}?'
