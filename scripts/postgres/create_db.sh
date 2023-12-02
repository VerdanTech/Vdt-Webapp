#!/bin/bash

db_name="$1"
user_name="$2"
user_password="$3"

echo "Switching to PostgreSQL user..."
sudo -i -u postgres psql <<EOF
CREATE DATABASE $db_name;
CREATE USER $user_name WITH ENCRYPTED PASSWORD '$user_password';
GRANT ALL PRIVILEGES ON DATABASE $db_name TO $user_name;
EOF