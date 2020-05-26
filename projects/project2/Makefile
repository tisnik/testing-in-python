PYTHON=python3

# can be pip, pip2, or pip3
PIP_TOOL=pip

TEST_TOOL=pytest

init:
	${PIP_TOOL} install -r requirements.txt

run:
	${PYTHON} main.py

test:
	${TEST_TOOL} -v tests

coverage:
	${TEST_TOOL} --cov=average --cov-report term-missing

coverage_report:
	${TEST_TOOL} --cov=average --cov-report html

clean:
	find . -type d -name __pycache__ -exec rm -r {} \+
	rm -rf .pytest_cache/
	rm -rf .benchmarks/
	rm .coverage

.PHONY: init test clean
