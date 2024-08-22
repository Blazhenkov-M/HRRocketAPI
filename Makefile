include .env

build:
	docker compose -f docker-compose-local.yaml build
up:
	make build
	docker compose -f docker-compose-local.yaml up -d
	make migrate
run:
	make build
	docker compose -f docker-compose-local.yaml up hr-rocket

down:
	docker compose -f docker-compose-local.yaml down

purge:
	docker compose -f docker-compose-local.yaml down -v && docker system prune --force --volumes