#!/bin/bash

set -e

CONNECT_URL="http://localhost:8083"
CONNECTOR_NAME="mysql-cdc"

echo "Checking if connector exists..."

STATUS=$(curl -s -o /dev/null -w "%{http_code}" \
  ${CONNECT_URL}/connectors/${CONNECTOR_NAME})

if [ "$STATUS" = "200" ]; then
    echo "Updating connector..."
    curl -X PUT \
      ${CONNECT_URL}/connectors/${CONNECTOR_NAME}/config \
      -H "Content-Type: application/json" \
      --data @debezium/mysql-cdc.json
else
    echo "Creating connector..."
    curl -X POST \
      ${CONNECT_URL}/connectors \
      -H "Content-Type: application/json" \
      --data @debezium/mysql-cdc.json
fi

echo
echo "Connector registration completed."