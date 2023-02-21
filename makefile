help:
	@echo
	@echo "使用:"
	@echo '    make [指令]'
	@echo
	@echo "指令:"
	@echo '    serve                启动服务，默认端口8080'
	@echo
	@echo "版本: 0.0.1"
	@echo

serve:
	uvicorn main:app --reload

build:
	docker build -t samzong/weblate-batch-scripts:latest .

.PHONY: serve help
