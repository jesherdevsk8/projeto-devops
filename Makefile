APP = projeto-devops

test:
	@flake8 . --exclude .venv
	@pytest -s -x -vv --cov=application --disable-warnings
	@coverage html

compose:
	@docker-compose down
	@docker-compose build
	@docker-compose up

heroku:
	@heroku container:login
	@heroku container:push -a $(APP) web
	@heroku container:release -a $(APP) web