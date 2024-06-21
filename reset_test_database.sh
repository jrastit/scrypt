#!/bin/bash
set -e

source venv/bin/activate

export SQLALCHEMY_SILENCE_UBER_WARNING=1
python3 reset_database.py
