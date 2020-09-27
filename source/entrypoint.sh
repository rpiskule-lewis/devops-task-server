#!/bin/sh

set -e

if [ "$DEBUG" == "true" ]; then
    echo "Debug enabled."
    set -x
else
    echo "Debug is disabled. Enable with DEBUG=true"
fi

GIT_REPO_FOLDER=/tmp/git-repo

cat motd.txt
if [ "$GIT_REPO" == "" ]; then
    echo "\$GIT_REPO must be defined."
    exit 1
fi

if [ "$BRANCH" == "" ]; then
    echo "\$BRANCH is undefined. Using master as default."
    BRANCH="master"
fi

if [ "$ROOT_FOLDER" == "" ]; then
    echo "\$ROOT_FOLDER is undefined. Using ./ as default"
fi

echo "Cloning $GIT_REPO..."
git clone $GIT_REPO $GIT_REPO_FOLDER

echo "Checking out $BRANCH..."
(cd $GIT_REPO_FOLDER && git checkout $BRANCH)

echo "Copying scripts from $ROOT_FOLDER..."
(cp -r $GIT_REPO_FOLDER/$ROOT_FOLDER/* /opt/scripts/)

echo "Changing Permissions..."
find /opt/scripts/ -iname "*.sh" | xargs -I input chmod 700 input

echo "Available Scripts:"
find /opt/scripts/ -iname "*.sh" | xargs -I input echo "  input"

echo "Starting Devops Task Server..."
# python3 ./helloworld.py
python3 manage.py runserver 0.0.0.0:8000
