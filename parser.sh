#!/bin/bash

if [ -z "$1" ]
then
echo "Missing the directory aurgument or missing the "/" at the end"
echo " Example /data/logs/"
fi
export LOGDIR=$1

TOP_5_USERS=`python3 now.py |sort  -nk 2 -r | head -5 | awk '{print $1,"   " $2,"   "$3,"    "$4,"   "$5}'`
echo "Total unique users: `python3.6 now.py |wc -l`"
echo "id         # pages # sess  longest shortest"
echo "$TOP_5_USERS"
