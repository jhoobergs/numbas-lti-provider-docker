#!/bin/bash
set -e

# Setup postgres
echo "Initialising new (empty) lti_provider"
mkdir -p /data/db && chown postgres:102 /data/db || echo "Dir /data/db already exists"
mkdir -p /data/log && chmod 777 /data/log || echo "Dir /data/log already exists"

mkdir -p /data/log/supervisor 
mkdir -p /data/log/nginx 

mkdir -p /data/other/media
mkdir -p /data/other/static

ln -s /data/other/media  /opt/numbas-lti-media 
ln -s /data/other/static /opt/numbas-lti-static 

# create media and static file directories
chown -R numbas_lti:numbas_lti /data/other/media
chown -R www-data:www-data /data/other/static
chmod -R 770 /data/other/*
chmod -R 775 /opt/numbas-lti-provider
sudo -u postgres /usr/lib/postgresql/12/bin/pg_ctl -D /data/db initdb

/etc/init.d/postgresql start
/etc/init.d/redis-server start
/etc/init.d/supervisor start
/etc/init.d/nginx start

sudo -u postgres psql -c "CREATE USER numbas_lti WITH ENCRYPTED PASSWORD '$POSTGRES_PASSWORD' CREATEDB;"
sudo -u postgres PGPASSWORD=$POSTGRES_PASSWORD createdb -U numbas_lti numbas_lti -h localhost


python3 install
