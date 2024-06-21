#!/bin/bash
set -e

source venv/bin/activate

gunicorn --bind 0.0.0.0:9431 server:app
