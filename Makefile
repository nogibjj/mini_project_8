# Makefile for setting up a Python project in GitHub Codespaces

# Name of your Python virtual environment folder
VENV_NAME = myenv

# The Python command to use. GitHub Codespaces often has `python3` installed.
PYTHON = python3

# Your main Python script to run
MAIN_SCRIPT = main.py

# Initialize GitHub Codespace environment
codespace-init: install
	# Any additional steps to set up your GitHub Codespace can go here

# Create a Python virtual environment
venv:
	$(PYTHON) -m venv $(VENV_NAME)

# Activate the virtual environment and install requirements
install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

# Run your main Python script within the virtual environment
run:
	. $(VENV_NAME)/bin/activate && $(PYTHON) $(MAIN_SCRIPT)

# Run tests
test:
	python -m pytest -vv --cov=main --cov=mylib test_*.py

# Format code
format:
	black *.py 

# Lint code
lint:
	pylint --disable=R,C --ignore-patterns=test_.*?py *.py

# Lint Dockerfile
container-lint:
	docker run --rm -i hadolint/hadolint < Dockerfile

# Refactor code
refactor: format lint

# Deploy application
deploy:
	# Deployment steps go here
		
# Run all tasks
all: install lint test format deploy

# Run all tasks specifically for Codespace
codespace-all: codespace-init all
