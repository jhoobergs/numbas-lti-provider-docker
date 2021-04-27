ARG VERSION=2.11-1

FROM python:3-slim-buster

ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update -y && apt-get upgrade -y && apt-get install -y --no-install-recommends apt-utils
RUN apt-get update -y && apt-get install -y git build-essential postgresql-server-dev-all

RUN useradd -ms /bin/bash numbas_lti && usermod -a -G numbas_lti www-data

RUN mkdir /srv/numbas-lti-media /srv/numbas-lti-static
RUN chown -R numbas_lti:numbas_lti /srv/numbas-lti-media
RUN chown -R www-data:www-data /srv/numbas-lti-static
RUN chmod -R 777 /srv/numbas-lti-media /srv/numbas-lti-static

RUN python3 -m pip install asgi_redis psycopg2 django-environ

ARG VERSION
RUN git clone https://github.com/numbas/numbas-lti-provider.git /srv/numbas-lti-provider
RUN chown -R numbas_lti:numbas_lti /srv/numbas-lti-provider
RUN chmod -R 770 /srv/numbas-lti-provider
RUN python3 -m pip install -r /srv/numbas-lti-provider/requirements.txt

COPY files/numbas-lti-provider/settings.py /srv/numbas-lti-provider/numbasltiprovider/settings.py
