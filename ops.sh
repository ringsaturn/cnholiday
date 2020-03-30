#!/bin/bash
SERVICE=$1

if [ x"$SERVICE" = x"test"  ]; then
    poetry install
    exec poetry run pytest tests/
fi
