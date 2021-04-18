#!/bin/bash
proc_name="ops11"
ops11=`ps aux | grep gunicorn | grep -v grep | wc -l`
if [ "$ops11" -eq 0 ]; then
 gunicorn -c config/gunicorn.conf.py $proc_name.wsgi:application
fi
sleep 1
echo $(ps aux | grep gunicorn | grep -v grep | wc -l)
