DOCKER_COMPOSE_BIN=docker compose
DOCKER_EXEC=$(DOCKER_COMPOSE_BIN) run --rm app sh -c
LINTER=flake8
APP_NAME=app
APP_DIRECTORY=.
FORMATTER_ARGS=-t py39 $(APP_DIRECTORY)
FORMATTER=black $(FORMATTER_ARGS)

lint:
	$(DOCKER_EXEC) "$(FORMATTER) && $(LINTER)"

.PHONY: test 
test:
	$(DOCKER_EXEC) "python -m unittest -v tests"

dc_build:
	$(DOCKER_COMPOSE_BIN) down && $(DOCKER_COMPOSE_BIN) build
