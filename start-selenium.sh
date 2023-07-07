#!/bin/bash

start (){
    docker run -d --rm \
        --name=selenium-container \
        -p 4444:4444 \
        selenium/standalone-chrome
}

stop (){
    docker kill selenium-container
}

check (){
    if [[ $(docker ps -f name=selenium-container --format '{{.Names}}') ]]; then
        echo 'Running...'
    else
        echo 'Not running'
    fi
}

if [ "$1" == "start" ]; then
    start

elif [ "$1" == "stop" ]; then
    stop
    sleep 1
elif [ "$1" == "check" ]; then
    check
else
    echo "Execute como: $0 <start|stop>"
fi