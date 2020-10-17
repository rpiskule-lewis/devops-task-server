#!/bin/sh

set -e

echo "Waiting 2 minutes for database to come online..."
eb -s "Connection refused" -e "x*1+5" -d 120 python3 testConnection.py
echo "Database Ready"

if [ "$DEBUG" == "true" ]; then
    echo "Debug enabled."
    set -x
else
    echo "Debug is disabled. Enable with DEBUG=true"
fi

if [ "$FIELD_ENCRYPTION_KEY" == "" ]; then
    echo "\$FIELD_ENCRYPTION_KEY must be defined. One auto-generated below."
    python3 generateSecret.py
    exit 1
fi

NEED_ADMIN_USER=false
if python3 databaseInit.py | grep "Created database"; then
    NEED_ADMIN_USER=true
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
find /opt/scripts/ -iname "*.sh" | xargs -I input -P10 chmod 700 input

echo "Available Scripts:"
find /opt/scripts/ -iname "*.sh" | xargs -I input echo "  input"

python3 manage.py makemigrations
python3 manage.py migrate

if [ "$NEED_ADMIN_USER" == "true" ]; then
    echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('admin', 'admin@myproject.com', 'password')" | python manage.py shell
fi

if [ "$WORKER" == "true" ]; then
    echo "Starting Devops Task Worker..."
    pwd
    celery -A pages worker -l INFO || true    
else
    echo "Starting Devops Task Server..."
    python3 manage.py runserver 0.0.0.0:8000
fi
