lint:
	mypy backend/

install:
	pip install -r requirements-dev.txt

run:
	uvicorn backend.main:app --reload

test: 
	python -m pytest backend/tests --verbose

mypy:
	mypy .

isort:
	isort .

ruff:
	ruff check .