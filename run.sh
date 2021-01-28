#!/bin/bash

if [ "$FLASK_ENV" == "development" ]; then
    gunicorn --bind "$FLASK_RUN_HOST:$FLASK_RUN_PORT" --worker-connections 2 --threads 4 --reload fsa_svc.server:app;
else
    gunicorn --bind "$FLASK_RUN_HOST:$PORT" -w 3 --max-requests 1000 --threads 4 fsa_svc.server:app;
fi
