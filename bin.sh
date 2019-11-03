#!/bin/bash
SERVICE=$1

if [ x"$SERVICE" = x"test"  ]; then
    poetry install
    exec poetry run pytest tests/
elif [ x"$SERVICE" = x"test-release"  ]; then
    rm -rf dist/
    poetry config repositories.test https://test.pypi.org/legacy/
    poetry publish --build --repository=test -vvv
elif [ x"$SERVICE" = x"release" ]; then
    rm -rf dist/
    exec poetry publish --build
fi
