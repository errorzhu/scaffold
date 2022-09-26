#!/bin/sh
root_dir=$(cd "$(dirname $0)";pwd)
root_dir=$(readlink -f "$root_dir")
work_dir=$(dirname $root_dir)
cd $work_dir
source $work_dir/bin/env.sh
######################main################

nohup java -DLOG_DIR=$APP_NAEM -cp "$work_dir/etc:$work_dir/*" org.springframework.boot.loader.JarLauncher > /dev/null 2>&1 &