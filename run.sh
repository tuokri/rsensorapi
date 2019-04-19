#!/usr/bin/env bash

export FLASK_ENV=development
export FLASK_APP="app/app.py:create_app('$1')"

flask run
