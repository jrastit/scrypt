#!/bin/bash
if [ "$(whoami)" != "postgres" ]; then
        echo "Script must be run as user: postgres"
        exit 255
fi

DB_USER="scrypt"
DB_NAME=$DB_USER
DB_PASSWORD=$1

psql -c "create user $DB_USER with encrypted password '$DB_PASSWORD'"

psql -c "create database $DB_NAME"
psql -c "grant all privileges on database $DB_NAME to $DB_USER"

psql -c "ALTER DATABASE $DB_NAME OWNER TO $DB_USER;"

psql -c "create database ${DB_NAME}_test"
psql -c "grant all privileges on database ${DB_NAME}_test to $DB_NAME"


psql -c "ALTER DATABASE ${DB_NAME}_test OWNER TO $DB_NAME;"