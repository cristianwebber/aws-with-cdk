export SHELL:=/bin/bash
export SHELLOPTS:=$(if $(SHELLOPTS),$(SHELLOPTS):)pipefail:errexit

.ONESHELL:

venv:
	test -d .venv || python3 -m venv .venv
	. .venv/bin/activate

clean:
	rm -rf .venv

init: clean venv
	pip install poetry
	poetry install

run:
	poetry run python python3 app.py
