all: install format test

documentation:
	myst build docs -o docs/_build

format:
	black . -l 79
	linecheck . --fix

check-vectorization:
	uv run python check_vectorization.py policyengine_au/variables

install:
	uv pip install --system -e .[dev]

test:
	uv run pytest policyengine_au/tests -v

test-cov:
	uv run pytest policyengine_au/tests --cov=policyengine_au --cov-report=term-missing

test-lite:
	uv run pytest policyengine_au/tests/policy -v

build:
	python -m build

changelog:
	build-changelog changelog.yaml --output CHANGELOG.md --start-from 0.1.0

clean:
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -delete
	rm -rf build dist *.egg-info .coverage htmlcov

.PHONY: all documentation format install test test-cov test-lite build changelog clean check-vectorization