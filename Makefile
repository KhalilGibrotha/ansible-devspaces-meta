.PHONY: help install install-dev test lint clean build

help:
	@echo "Available targets:"
	@echo "  install       - Install the package"
	@echo "  install-dev   - Install the package with development dependencies"
	@echo "  test          - Run tests"
	@echo "  lint          - Run linters"
	@echo "  clean         - Remove build artifacts"
	@echo "  build         - Build the package"

install:
	pip install -e .

install-dev:
	pip install -e .[dev]

test:
	pytest

lint:
	ansible-lint examples/ || true
	python -m pylint ansible_devspaces || true

clean:
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete

build: clean
	python -m build
