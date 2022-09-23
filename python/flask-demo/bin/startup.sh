#!/bin/bash
root_dir=$(cd "$(dirname $0)";pwd)
root_dir=$(readlink -f "$root_dir")
work_dir=$(dirname $root_dir)

source $work_dir/bin/env.sh
#set a  log dir
log_dir=$work_dir/logs

################subsitute log dir#############################
if [ ! -d $log_dir ]; then
  mkdir -p $log_dir
fi

cd $log_dir
log_dir=`pwd`
sed -i "s#@log_dir@#$log_dir#g" $work_dir/etc/config.py
sed -i "s#@log_dir@#$log_dir#g" $work_dir/etc/gunicorn.py
sed -i "s#@log_dir@#$log_dir#g" $work_dir/etc/logging.conf


##########substitute gunicorn configuration#######################
sed -i "s#@work_dir@#$work_dir#g" $work_dir/etc/gunicorn.py
sed -i "s#@work_dir@#$work_dir#g" $work_dir/etc/logging.conf


######################main################
if [ -f $work_dir/pid ];then
  echo $APP_NAME"already started !!!"
  exit 0
fi

#gunicorn -D  --log-config  $work_dir/etc/logging.conf --chdir $work_dir/ddc_api/  -c $work_dir/etc/gunicorn.py   main:app
gunicorn -D  --log-config  $work_dir/etc/logging.conf --chdir $work_dir/  -c $work_dir/etc/gunicorn.py   $APP_NAME.main:app
sleep 3

if [ ! -f $work_dir/pid  ];then
   echo $APP_NAME'failed ,please check logs  !!!!'
   exit 255
fi

oldpid=`cat $work_dir/pid`

pid=$(ps -p $oldpid | tail -1 | awk '{ print $1 }')

if echo $pid | egrep -q '^[0-9]+$'; then
    echo $APP_NAME"started successful !!!!"
else
    rm -f $work_dir/pid
    echo $APP_NAME'failed ,please check logs  !!!!'
fi




