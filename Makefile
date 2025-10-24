# Makefile for GeminiDecode

# Variables
PYTHON := python3
PIP := pip
PROJECT_NAME := gemini-decode

# Default target
.PHONY: help
help:
	@echo "Available targets:"
	@echo "  install     - Install the package in development mode"
	@echo "  run         - Run the Streamlit application"
	@echo "  test        - Run tests"
	@echo "  lint        - Run code linting"
	@echo "  format      - Format code with black"
	@echo "  clean       - Clean build artifacts"
	@echo "  deps        - Install dependencies"
	@echo "  deps-dev    - Install development dependencies"
	@echo "  build       - Build the package"
	@echo "  publish     - Publish the package to PyPI"

# Install package in development mode
.PHONY: install
install:
	$(PIP) install -e .

# Run the Streamlit application
.PHONY: run
run:
	streamlit run app.py

# Run tests
.PHONY: test
test:
	$(PYTHON) -m pytest tests/

# Run code linting
.PHONY: lint
lint:
	$(PYTHON) -m flake8 .
	$(PYTHON) -m mypy .

# Format code with black
.PHONY: format
format:
	$(PYTHON) -m black .

# Clean build artifacts
.PHONY: clean
clean:
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info/
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -delete

# Install dependencies
.PHONY: deps
deps:
	$(PIP) install -r requirements.txt

# Install development dependencies
.PHONY: deps-dev
deps-dev:
	$(PIP) install -r requirements.txt
	$(PIP) install pytest black flake8 mypy

# Build the package
.PHONY: build
build:
	$(PYTHON) setup.py sdist bdist_wheel

# Publish the package to PyPI
.PHONY: publish
publish:
	$(PYTHON) -m twine upload dist/*

# Install all dependencies and set up development environment
.PHONY: dev-setup
dev-setup: deps deps-dev install

# Run all checks
.PHONY: check
check: lint test