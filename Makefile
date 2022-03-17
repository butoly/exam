all: build

build:
	docker build -t app:latest -f ops/Dockerfile .
