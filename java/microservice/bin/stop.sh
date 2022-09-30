#!/bin/sh
root_dir=$(cd "$(dirname $0)";pwd)
root_dir=$(readlink -f "$root_dir")
work_dir=$(dirname $root_dir)
cd $work_dir
source $work_dir/bin/env.sh
######################main################
ps -ef | grep $APP_NAME | grep -v grep |head -n 1 | awk '{print $2}' |xargs kill -15
if [ $? == 0 ] ;then echo $APP_NAME"stop success" ;fi