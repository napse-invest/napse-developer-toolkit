build:
	docker compose -f backend/docker/development.yml build

up:
	docker compose -f backend/docker/development.yml up -d --build --remove-orphans

down:
	docker compose -f backend/docker/development.yml down

in:
	docker exec -it napse_dtk_dev_django bash

test-napse:
	docker exec napse_dtk_dev_django python manage.py test -v2

coverage:
	docker exec napse_dtk_dev_django coverage run manage.py test -v2 --keepdb && docker exec napse_dtk_dev_django coverage html && docker exec napse_dtk_dev_django coverage report

coverage-open:
	docker exec napse_dtk_dev_django coverage run manage.py test -v2 --keepdb && docker exec napse_dtk_dev_django coverage html && docker exec napse_dtk_dev_django coverage report && open htmlcov/index.html