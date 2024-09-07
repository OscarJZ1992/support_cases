#!/bin/bash

REQUIREMENTS_FILE="requirements.txt"

echo "Instalando dependencias de Python..."
pip install -r $REQUIREMENTS_FILE


#DB config
DB_USER="postgres"
DB_PASSWORD="1234"
DB_NAME="support_process_cases"

export PGPASSWORD=$DB_PASSWORD

echo "Dropping database if it exists..."
psql -U $DB_USER -h localhost -p 5432 -c "DROP DATABASE IF EXISTS $DB_NAME;"

echo "Creating database..."
psql -U $DB_USER -h localhost -p 5432 -c "CREATE DATABASE $DB_NAME;"

echo "Creating tables..."
psql -U $DB_USER -h localhost -p 5432 -d $DB_NAME -f api/data/create_tables.sql

unset PGPASSWORD

echo "Base de datos y tablas creadas correctamente."