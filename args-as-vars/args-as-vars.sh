#!/usr/bin/env bash
#TODO: handle linebreaks, add checks and probably relax some constraints, add logger

regex='^[A-Za-z0-9_]+=.+$'

for arg in "$@"; do
    if [[ "$arg" =~ $regex ]]; then
        pname=$(echo "$arg" | cut -d '=' -f 1)
        pvalue=$(echo "$arg" | cut -d '=' -f 2)
        eval "$pname='$pvalue'"
        echo "$(date '+%F %k:%M:%S') Initialized parameter '$pname' with value '$pvalue'"
    fi
done

unset regex