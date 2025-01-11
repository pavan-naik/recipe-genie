install:
	pip install -e .
	pip install -r requirements.txt

lint:
	black src tests
	flake8 src tests
	PYTHONPATH=. pylint src/ tests/
	mypy src tests

test:
	pytest tests/ -v --cov=src/ --cov-report=term-missing

clean:
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete

all: install lint test clean