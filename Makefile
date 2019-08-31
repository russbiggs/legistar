.PHONY: docs

init:
	pip install pipenv --upgrade
	pipenv install --dev

clean:
	rm -rf dist/*

test:
	mypy
	nose2 -v

docs:
	$(MAKE) -C docs html

publish:
	python setup.py sdist bdist_wheel
	pipenv run twine upload dist/*
	$(MAKE) clean

