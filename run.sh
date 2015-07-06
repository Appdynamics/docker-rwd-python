#!/bin/bash

docker run -e RWD_URL=$RWD_URL \
    -e RWD_PORT=$RWD_PORT \
    -e RWD_USERNAME=$RWD_USERNAME \
    -e RWD_ACCESSKEY=$RWD_ACCESSKEY \
        appdynamics/rwd-python $@
