docker network create --driver bridge local || true
docker rm postgres
docker run -it -p 5432:5432 --network=local --name postgres -e POSTGRES_PASSWORD=password postgres:11.9-alpine
