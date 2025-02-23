# Docker Compose Recipe for Numbas LTI Tool

This repository contains a recipe to run the [Numbas LTI tool provider](https://numbas-lti-provider.readthedocs.io/en/latest/) in Docker.

It contains everything needed to run the Numbas LTI tool in Docker containers.

## Documentation

There's documentation for administrators, instructors and students at [numbas-lti-provider.readthedocs.io](https://numbas-lti-provider.readthedocs.io/).

## Installation

### Prerequisites

Install [Docker](https://docs.docker.com/engine/install/) and [Docker Compose](https://docs.docker.com/compose/install/) on your server.

### Setup

Copy the file `settings.env.dist` to `settings.env` and write your own values each of the variables inside.

Run the `get_secret_key` script to generate a value for the `SECRET_KEY` environment variable, and put that in `settings.env`:

```
docker-compose run --rm numbas-setup python ./get_secret_key
```

Obtain an SSL certificate and key for the domain you will access the Numbas LTI provider from. Copy the key to `files/ssl/numbas-lti.key` and the certificate to `files/ssl/numbas-lti.pem`.

Run the installation script, to set up the database and create the superuser account:

```
docker-compose run --rm numbas-setup python ./install
```

The LTI provider is ready to start.

### Starting

Run the following command:

```
docker-compose up --scale daphne=4 --scale huey=2
```

You can customise the number of each of the kinds of process by changing the numbers in the `--scale` arguments.
The `daphne` process handles web requests; you will need more if you have lots of simultaneous connections.
The `huey` process runs asynchronous tasks; you will need more if you find that tasks such as reporting scores or generating report files take a very long time.

### Stopping

Stop the numbas-lti containers with `docker-compose down`.

## Running in the cloud

Docker Compose files can also be used to deploy to the cloud. See the following documents for more information about deploying Docker to the cloud:

- [Compose for Amazon ECS](https://docs.docker.com/engine/context/ecs-integration/)
- [Compose for Microsoft ACI](https://docs.docker.com/engine/context/aci-integration/)

## Upgrading

When there is a new version of the Numbas LTI provider, you must rebuild the Docker image and apply any database migrations.

If any other changes are required when moving to a particular version, they will be listed here.

### Standard upgrade instructions

To upgrade to a new version, follow these steps after fetching the latest version of this repository.

Remake the container images:

```
docker-compose build --no-cache numbas-setup
docker-compose build --no-cache daphne
docker-compose build --no-cache huey
```

Then run the installation script again:

```
docker-compose run --rm numbas-setup python ./install
```

### v2.x to v3.0

There are several new settings which must be set in `settings.env`.
Look at `settings.env.dist` to see what they are, copy them across to your `settings.env` file, and make changes if needed.

# Standalone

## Building

- `docker build --file Dockerfile-self-contained -t lti-test .`

### Options

- Choosing the repo to get the lti provider from: `docker build --file Dockerfile-self-contained -t lti-test --build-arg NUMBAS_LTI_REPO="https://github.com/jhoobergs/numbas-lti-provider.git " .`
- You can also specify a `NUMBAS_LTI_BRANCH` to change the branch

## Running

Make sure that you copied `settings.env.dist`to `settings.env` and changed the values. This env variable will need to be set.

### Running setup

- `docker run --rm --volume numbas_lti:/data --entrypoint bash --env-file settings.env lti-test setup.sh`

### Running

- Create the volume (once): `docker volume create numbas_lti`
- There should be a volume mounted to `/data`
- `docker run --rm --volume numbas_lti:/data --env-file settings.env -p 80:80 lti-test`

### Updating after new version

- `docker run --rm --volume numbas_lti:/data --entrypoint bash --env-file settings.env lti-test update.sh`
- Runs migration and generation of static files
