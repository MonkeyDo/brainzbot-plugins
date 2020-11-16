import json

from ..base import BasePlugin
from ..decorators import listens_to_command, listens_to_regex_command


class Plugin(BasePlugin):
    """
    More advanced version of the brainz plugin using the new
    listens_to_regex_command decorator.

    Remembers and recalls arbitrary information.

    To have me remember something for you, ask me in this format:

        {{ command_prefix }}remember thing=stuff I need to remember

    When you want me to recall the information, ask me in this format:

        {{ command_prefix }}recall thing

    I will prompty respond to your request with:

        stuff I need to remember

    To make me forget something use

        {{ command_prefix }}forget thing

    To display all the things I've remembered use

        {{ command_prefix }}braindump
    """

    @listens_to_regex_command("remember", r"(?P<key>.+?)\s*=\s*(?P<value>.*)")
    def remember(self, line, key, value):
        try:
            memory = json.loads(self.retrieve("memory"))
        except TypeError:
            memory = []

        memory.append(key)

        self.store("memory", json.dumps(memory))

        self.store(key, value)
        return f'I will remember "{key}" for you {line.user}.'

    @listens_to_regex_command("recall", r"(?P<key>.*)")
    def recall(self, line, key):
        value = self.retrieve(key)
        if value:
            return value
        else:
            return f'I\'m sorry, I don\'t remember "{key}", are you sure I should know about it?'

    @listens_to_regex_command("forget", r"(?P<key>.*)")
    def forget(self, line, key):
        try:
            memory = json.loads(self.retrieve("memory"))
        except TypeError:
            memory = []

        if key not in memory:
            return f'I\'m sorry, I don\'t remember "{key}", are you sure I should know about it?'

        memory.remove(key)
        self.store("memory", json.dumps(memory))

        self.delete(key)
        return f'What was "{key}" all about?'

    @listens_to_command("braindump")
    def braindump(self, line, args):
        try:
            memory = json.loads(self.retrieve("memory"))
        except TypeError:
            memory = []

        if len(memory) == 0:
            return "I have no memory yet, use the recall command to make me remember stuff for you."
        elif len(memory) == 1:
            return f'I remember "{memory[0]}".'
        else:
            return 'I remember "{0}" and "{1}".'.format('", "'.join(memory[:-1]), memory[-1])
