#!/bin/bash
SERVICE=$1

if [ x"$SERVICE" = x"test"  ]; then
    poetry install
    exec poetry run pytest tests/
elif [ x"$SERVICE" = x"tests"  ]; then
    poetry install
    exec poetry run pytest tests/
elif [ x"$SERVICE" = x"test-release" ]; then
    rm -rf dist/
    poetry config repositories.test https://test.pypi.org/simple
    exec poetry publish --build --repository=test
elif [ x"$SERVICE" = x"release" ]; then
    exec poetry publish --build
fi
