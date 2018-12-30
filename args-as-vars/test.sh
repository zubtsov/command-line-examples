#!/usr/bin/env bash
#USAGE: ./test.sh first=<value> second=<value> third=<value>

source args-as-vars.sh

echo "Passed named arguments:"
echo "first=$first"
echo "second=$second"
echo "third=$third"
echo "regex=$regex" #should be empty