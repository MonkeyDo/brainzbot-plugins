#!/usr/bin/env python
from setuptools import setup, find_packages

setup(
    name='brainzbot_plugins',
    version='1.0',
    description="Plugins and service integrations for BrainzBot",
    author="MetaBrainz",
    url='https://github.com/metabrainz/brainzbot-plugins',
    packages=find_packages(),
    scripts=['bin/botbot-shell'],
)
