#!/bin/bash
root_dir=$(cd "$(dirname $0)";pwd)
root_dir=$(readlink -f "$root_dir")
work_dir=$(dirname $root_dir)
source $work_dir/bin/env.sh

export FLASK_APP=manage.py
cd $work_dir/$APP_NAME
######################main################
flask db init
flask db migrate
#flask db upgrade
