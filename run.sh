#!/bin/bash

ln -s /data/other/media  /opt/numbas-lti-media
ln -s /data/other/static /opt/numbas-lti-static

/etc/init.d/postgresql start
/etc/init.d/redis-server start
/etc/init.d/supervisor start
/etc/init.d/nginx start

tail -f /data/log/**/*
