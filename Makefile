.PHONY: db

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
	python -m pytest -s -v tests
# cargo test --no-default-features