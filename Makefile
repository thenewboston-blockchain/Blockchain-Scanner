.PHONY: up-dependencies-only
up-dependencies-only:
	docker-compose -f docker-compose.yml up --force-recreate nano