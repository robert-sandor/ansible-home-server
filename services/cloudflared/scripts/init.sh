#!/bin/bash

docker run --rm \
    -v $pwd:/etc/cloudflared \
    msnelling/cloudflared \
    /usr/local/bin/cloudflared tunnel login 

docker run --rm \
    -v $pwd:/etc/cloudflared \
    msnelling/cloudflared \
    /usr/local/bin/cloudflared tunnel create $1
