#!/bin/bash

export DD_SERVICE="webapp-extension"
export DD_ENV="dev"
export DD_VERSION="1.0.0"
export DD_LOGS_INJECTION=true
export DD_TRACE_ENABLED=true
export WEBAPP_HOST="0.0.0.0"
export WEBAPP_PORT="8081"

poetry run ddtrace-run uvicorn webapp_extension.main:app --host "$WEBAPP_HOST" --port $WEBAPP_PORT
