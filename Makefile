build:
	docker compose -f backend/docker/development.yml build --remove-orphans

up:
	docker compose -f backend/docker/development.yml up -d --build --remove-orphans

down:
	docker compose -f backend/docker/development.yml down
