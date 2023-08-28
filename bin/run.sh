#!/usr/bin/env bash

gunicorn wsgi:application --bind 0.0.0.0:8080 --log-level=debug --workers=4