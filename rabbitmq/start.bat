docker network create --driver bridge local || true
docker rm rabbitmq
docker run -it -p 5672:5672 --network=local --name rabbitmq rabbitmq:3.8.9-alpine

