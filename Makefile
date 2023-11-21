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

down:
	docker compose -f backend/docker/development-${IMAGE}.yml down

in:
	docker exec -it napse_dtk_dev_django bash

test-napse:
	docker exec napse_dtk_dev_django python manage.py test -v2

coverage:
	docker exec napse_dtk_dev_django coverage run manage.py test -v2 --keepdb && docker exec napse_dtk_dev_django coverage html && docker exec napse_dtk_dev_django coverage report

coverage-open:
	docker exec napse_dtk_dev_django coverage run manage.py test -v2 --keepdb && docker exec napse_dtk_dev_django coverage html && docker exec napse_dtk_dev_django coverage report && open htmlcov/index.html

litestream:
	set -a && . ./backend/.envs/.development/.litestream && set +a && litestream replicate --config backend/docker/compose/production/litestream/config.yml

