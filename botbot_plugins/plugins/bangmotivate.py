from ..base import BasePlugin
from ..decorators import listens_to_all


class Plugin(BasePlugin):
    """
    Notifies people of the excellent work they are doing.

    Let me know who is doing good work:

        !m {{ nick }}

    And I will promptly notify them:

        You are doing good work {{ nick }}

    http://motivate.im/
    """

    @listens_to_all(r'^\!m (?P<nick>.+?)$')
    def motivate(self, line, nick):
        return f"You're doing good work, {nick}!"
