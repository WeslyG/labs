.PHONY: deps test

reqs:
	pip3 install virtualenv

deps: reqs
	python3 -m venv .venv; \
	. .venv/bin/activate; \
	pip3 install -r requirements.txt

test:
	. .venv/bin/activate; \
	pytest