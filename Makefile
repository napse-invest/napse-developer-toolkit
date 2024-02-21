SHELL := /bin/bash
IMAGE ?= postgres
OS := $(shell uname)

all: up

setup:
ifeq ($(OS),Darwin)        # Mac OS X
	./setup-osx.sh
else ifeq ($(OS),Linux)
	./setup-unix.sh
else 
	./setup-windows.sh
endif

build:
	docker compose -f backend/docker/development-${IMAGE}.yml build 

up:
	docker compose -f backend/docker/development-${IMAGE}.yml up -d --build --remove-orphans

up-prod:
	docker compose -f backend/docker/production.yml up -d --build --remove-orphans

up-no-docker:
	export DB_SETUP=litestream
	export DB_ENGINE=SQLITE
	export USE_DOCKER=no
	export IPYTHONDIR=/app/.ipython
	export REDIS_URL=redis://redis:6379/0 
	export DJANGO_SETTINGS_MODULE=config.settings.development
	export DJANGO_SECRET_KEY=not_so_secret
	export DJANGO_DEBUG=True 
	export IS_LOCAL=True
	python backend/manage.py makemigrations
	python backend/manage.py migrate
	python backend/manage.py runserver_plus

down:
	docker compose -f backend/docker/development-${IMAGE}.yml down

clean:
	docker compose -f backend/docker/development-${IMAGE}.yml down -v --remove-orphans && rm backend/db/db.sqlite3

in:
	docker exec -it napse_dtk_dev_django bash

test:
	docker exec napse_dtk_dev_django python manage.py test -v2

coverage:
	docker exec napse_dtk_dev_django coverage run manage.py test -v2 --keepdb && docker exec napse_dtk_dev_django coverage html && docker exec napse_dtk_dev_django coverage report

coverage-open:
	docker exec napse_dtk_dev_django coverage run manage.py test -v2 --keepdb && docker exec napse_dtk_dev_django coverage html && docker exec napse_dtk_dev_django coverage report && open htmlcov/index.html

litestream:
	set -a && . ./backend/.envs/.development/.litestream && set +a && litestream replicate --config backend/docker/compose/production/litestream/config.yml

setup-prod:
	./backend/docker/setup-prod.sh

build-prod: setup-prod
	docker compose -f backend/docker/production.yml build