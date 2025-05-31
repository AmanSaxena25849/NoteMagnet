#!/bin/bash

# Install Python dependencies
pip install -r requirements.txt

# Collect static files
python3 manage.py collectstatic --noinput