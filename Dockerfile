FROM metabrainz/brainzbot-core

WORKDIR /plugins

COPY Pipfile Pipfile.lock ./
RUN set -ex && pipenv install --deploy --system

COPY . ./
RUN python setup.py install

WORKDIR /core

CMD ["run_plugins", "--settings=botbot.settings"]
