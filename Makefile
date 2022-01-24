test:
	pipenv run py.test tests


run:
	pipenv run flask run

lint:
	pipenv run black api tests
	pipenv run isort api tests