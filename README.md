# BrainzBot Chatlogger Plugins

To get started:

```
$ pip install -e git+https://github.com/metabrainz/brainzbot-plugins.git#egg=brainzbot-plugins
$ brainzbot-shell
```

Pass a comma-separated list of modules to run a subset of the plugins:

```
$ brainzbot-shell metabrain,images
```

## Tests

[![Build Status](https://travis-ci.org/metabrainz/brainzbot-plugins.svg?branch=master)](https://travis-ci.org/metabrainz/brainzbot-plugins/)

```
py.test brainzbot_plugins
```

## Contribute!

We want you to contribute your own plugins to make BrainzBot better. Please [read the docs](https://github.com/metabrainz/brainzbot-plugins/blob/master/DOCS.md) and review our [contributing guidelines](https://github.com/metabrainz/brainzbot-plugins/blob/master/CONTRIBUTING.md) prior to getting started to ensure your plugin is accepted.
