#!/usr/bin/bash
set -e
export DEBIAN_FRONTEND="noninteractive"

# create the virtualenv for the python modules
# virtualenv -p python3 /opt/numbas_lti_python
# chown -R numbas_lti:numbas_lti /opt/numbas_lti_python
# chmod -R 770 /opt/numbas_lti_python

# install python modules
cd /opt/numbas-lti-provider
#source /opt/numbas_lti_python/bin/activate
python3 -m pip install -r requirements.txt
python3 -m pip install channels_redis==3.3.0 psycopg2==2.8.6

/etc/init.d/postgresql start
/etc/init.d/redis-server start

# Setup nginx and supervisor
#/etc/init.d/supervisor start
#/etc/init.d/nginx start
