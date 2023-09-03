#!/usr/bin/env bash

gunicorn wsgi:application --bind 0.0.0.0:8000 --log-level=debug --workers=4