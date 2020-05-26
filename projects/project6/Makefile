PYTHON=python3

# can be pip, pip2, or pip3
PIP_TOOL=pip

TEST_TOOL=pytest

help: ## Show this help screen
	@echo 'Usage: make <OPTIONS> ... <TARGETS>'
	@echo ''
	@echo 'Available targets are:'
	@echo ''
	@grep -E '^[ a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | \
		awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'
	@echo ''

init: ## Install this project using pip tool
	${PIP_TOOL} install -r requirements.txt

run: ## Run project
	${PYTHON} main.py

test: ## Test the project (run unit tests)
	${TEST_TOOL} -v --pyargs average

coverage: ## Display test code coverage
	${TEST_TOOL} --cov=average --cov-report term-missing

coverage_report: ## Generate code coverage report
	${TEST_TOOL} --cov=average --cov-report html

clean: ## Cleanup repository
	find . -type d -name __pycache__ -exec rm -r {} \+
	rm -rf .pytest_cache/
	rm -rf .benchmarks/
	rm .coverage

.PHONY: init test clean help
