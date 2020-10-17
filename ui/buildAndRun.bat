call build.bat
docker network create --driver bridge local || true
docker run -it -p 8000:8000 --network=local --env FIELD_ENCRYPTION_KEY=67223aa368643276aa724674a2959bc4aa878d266adfe2bf5b91a0c99731c1a8 --env GIT_REPO=https://github.com/rpiskule-lewis/devops-task-server.git --env BRANCH=master --env ROOT_FOLDER=scripts local
