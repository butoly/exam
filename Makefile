all: build

build:
	docker build -t app:latest -f ops/Dockerfile .

start:
    docker run -p 8000:8000 -v ${PWD}:/app app
