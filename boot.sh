#!/bin/bash
cd flask/
source bin/activate
exec gunicorn -b :5000 --access-logfile - --error-logfile - app:app