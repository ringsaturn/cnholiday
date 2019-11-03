#!/bin/bash
SERVICE=$1

if [ x"$SERVICE" = x"test"  ]; then
    poetry install
    exec poetry run pytest tests/
elif [ x"$SERVICE" = x"tests"  ]; then
    poetry install
    exec poetry run pytest tests/
elif [ x"$SERVICE" = x"release" ]; then
    rm -rf dist/
    exec poetry publish --build
fi
