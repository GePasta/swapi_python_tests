# swapi_python_tests
Testing Python clone of SWAPI REST API. This project was created and tested on macOS and Linux.
It should be able to work correctly on Windows, but it wasn't tested.


# How to run
## Type from main folder:
- `make build` to build docker container
- `make test` to run all tests

### In order to run only functional tests type `make functional`. 
### In order to run only performance tests type `make performance`

# Project technology stack:
- HTTP Server: FlaskAPI
- Testing Framework: Pytest
- Performance testing lib: Pytest-benchmark
- SCA: mypy, flake8, flake8-quotes
- Report creation: pytest-html

# Logging
- HTTP server is logging in all incoming requests and response codes in `./results` folder.
- While running functional tests an additional `html` report is created.

# Functional tests:
- Tests are validating three endpoints `/people`, `/planets`, `/starships`,
- For each endpoint tests are checking `item_ids` e.g. `/people/1`. For id check we've got positive and negative scenarios.

# Performance tests:
- Tests are validating the `/planets` endpoint with id's starting from `1` and ending on `100`. Each id is tested for 2 s. 