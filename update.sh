#!/bin/bash
set -e


/etc/init.d/postgresql start
/etc/init.d/redis-server start
/etc/init.d/supervisor start
/etc/init.d/nginx start

cd /opt/numbas-lti-provider
python3 manage.py migrate
python3 manage.py collectstatic --noinput
