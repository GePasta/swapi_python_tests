#-include env/local.env
#export

.PHONY: build
build:
	docker build  -f ./docker/Dockerfile -t http-server-tests:ci .

.PHONY: shell
shell:
	docker run -v ${CURDIR}:/usr/local/main -it http-server-tests:ci bash

RESULTS_PATH:=${CURDIR}/results
TIMESTAMP:=$(shell date +%Y%m%d_%H%M%S)

.PHONY: test
test:
	pytest \
	--log-file=${RESULTS_PATH}/${TIMESTAMP}_tests.log \
	--html=${RESULTS_PATH}/${TIMESTAMP}_report.html --self-contained-html \
	$(filter-out $@,$(MAKECMDGOALS))
