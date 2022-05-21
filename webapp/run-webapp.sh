#!/bin/bash

export DD_SERVICE="webapp"
export DD_ENV="dev"
export DD_VERSION="1.0.0"
export DD_LOGS_INJECTION=true
export DD_TRACE_ENABLED=true
export WEBAPP_HOST="0.0.0.0"
export WEBAPP_PORT="8080"

poetry run ddtrace-run uvicorn webapp.main:app --host "$WEBAPP_HOST" --port "$WEBAPP_PORT"
#poetry run ddtrace-run gunicorn -k uvicorn.workers.UvicornWorker webapp.main:app -w 1 -b "$WEBAPP_HOST:$WEBAPP_PORT"
#poetry run uvicorn webapp.main:app --host "$WEBAPP_HOST" --port $WEBAPP_PORT
