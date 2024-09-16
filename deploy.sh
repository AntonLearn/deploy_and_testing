#!/bin/bash
cd /opt/dj_prj
git pull origin master
source env/bin/activate
pip install -r requirements.txt
python manage.py migrate
sudo systemctl restart gunicorn
sudo systemctl daemon-reload
