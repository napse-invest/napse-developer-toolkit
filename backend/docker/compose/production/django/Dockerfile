# pull official base image
ARG PYTHON_VERSION=3.11-slim-bullseye

FROM ubuntu:22.04 as ubuntu-build-stage
ARG BUILD_ENVIRONMENT=production
ARG APP_HOME=/app

# set work directory
WORKDIR ${APP_HOME}
RUN apt-get update && apt-get install --no-install-recommends -y \
  # psycopg2 dependencies
  libpq-dev \
  # Translations dependencies
  gettext \
  # wget 
  wget \
  # cleaning up unused files
  && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
  && rm -rf /var/lib/apt/lists/*
RUN apt-get update && apt-get install -y ca-certificates && update-ca-certificates
RUN wget https://github.com/benbjohnson/litestream/releases/download/v0.3.13/litestream-v0.3.13-linux-amd64.deb
RUN dpkg -i litestream-v0.3.13-linux-amd64.deb


FROM python:${PYTHON_VERSION} as python
COPY --from=ubuntu-build-stage /usr/bin/litestream /usr/bin/litestream

# ----------------------------------------------------------------------------------------
# Python build stage
FROM python as python-build-stage
ARG BUILD_ENVIRONMENT=production
RUN /usr/bin/litestream version
# Update and install 
RUN apt-get update && apt-get install --no-install-recommends -y \
  # psycopg2 dependencies
  libpq-dev \
  # Translations dependencies
  gettext \
  # cleaning up unused files
  && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
  && rm -rf /var/lib/apt/lists/*

# Create Python Dependency and Sub-Dependency Wheels.
COPY ./requirements .
RUN pip wheel --wheel-dir /usr/src/app/wheels \
    -r ${BUILD_ENVIRONMENT}.txt


# ----------------------------------------------------------------------------------------
# Python 'run' stage
FROM python as python-run-stage

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ARG BUILD_ENVIRONMENT=production
ARG APP_HOME=/app

# set work directory
WORKDIR ${APP_HOME}

# Install required system dependencies
RUN apt-get update && apt-get install --no-install-recommends -y \
  # psycopg2 dependencies
  libpq-dev \
  # Translations dependencies
  gettext \
  # cleaning up unused files
  && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
  && rm -rf /var/lib/apt/lists/*

# All absolute dir copies ignore workdir instruction. All relative dir copies are wrt to the workdir instruction
# copy python dependency wheels from python-build-stage
COPY --from=python-build-stage /usr/src/app/wheels  /wheels/

# use wheels to install python dependencies
RUN pip install --no-cache-dir --no-index --find-links=/wheels/ /wheels/* \
	&& rm -rf /wheels/


# Commands
COPY ./docker/compose/${BUILD_ENVIRONMENT}/django/start /start
RUN sed -i 's/\r$//g' /start
RUN chmod +x /start

COPY ./docker/compose/${BUILD_ENVIRONMENT}/django/entrypoint /entrypoint
RUN sed -i 's/\r$//g' /entrypoint
RUN chmod +x /entrypoint

COPY ./docker/wait-for-it.sh /wait-for-it.sh
RUN sed -i 's/\r$//g' /wait-for-it.sh
RUN chmod +x /wait-for-it.sh

COPY ./docker/compose/${BUILD_ENVIRONMENT}/django/celery/worker/start /start-celeryworker
RUN sed -i 's/\r$//g' /start-celeryworker
RUN chmod +x /start-celeryworker

COPY ./docker/compose/${BUILD_ENVIRONMENT}/django/celery/beat/start /start-celerybeat
RUN sed -i 's/\r$//g' /start-celerybeat
RUN chmod +x /start-celerybeat

COPY ./docker/compose/${BUILD_ENVIRONMENT}/litestream/config.yml /etc/litestream.yml

# Copy everything
COPY . .

ENTRYPOINT ["/entrypoint"]