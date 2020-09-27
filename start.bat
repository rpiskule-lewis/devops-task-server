call build.bat
docker run -it -p 8000:8000 --env GIT_REPO=https://github.com/rpiskule-lewis/devops-task-server.git --env BRANCH=master --env ROOT_FOLDER=scripts local
