SHELL := /bin/bash

# .PHONY: db

# Check python formatting
check-style:
	black --check --line-length 100 --target-version py38 py_src/navsearch tests

# Clean repo of all build artifacts
clean:
	rm -rf build build-env dist target
	rm -rf py_src/navsearch.egg-info
	rm -rf py_src/hello_rust

# Build Postgres Database
# db:
# 	docker-compose --project-name wikimap up

# Format python code
style:
	black --line-length 100 --target-version py38 py_src/navsearch tests

# Run test suite
test:
	source activate-env; \
	python -m pytest -s -v tests; \
	cargo test --no-default-features

install-dev:
	source activate-env; \
	./build-wheel.sh; \
	python -m pip install --force-reinstall dist/navsearch-*; \

tika-container:
	docker-compose build --build-arg USER_ID=1000 --build-arg GROUP_ID=1000