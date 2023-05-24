CONTAINER_NAME ?= weblate-scripts

help:
	@echo
	@echo "使用:"
	@echo '    make [指令]'
	@echo
	@echo "指令:"
	@echo '    build                build 最新版本的镜像'
	@echo '    stop                 停止已有容器'
	@echo '    start                启动容器，运行在端口 http://127.0.0.1:8888'
	@echo
	@echo "版本: 1.1.0"
	@echo

build:
	docker build -t samzong/weblate-batch-scripts:latest .

build-release:
	docker build --push -t release.daocloud.io/ndx-product/weblate-batch-scripts:latest .

stop:
	docker container rm -f ${CONTAINER_NAME}

start:
	docker run -d --name ${CONTAINER_NAME} -p 8888:8888 samzong/weblate-batch-scripts:latest
	echo "Visit: http://127.0.0.1:8888"

.PHONY: build build-release stop start help
