#!/bin/sh

DATE=$(date +%Y%m%d)

mkdir -p /var/log/nginx/$DATE

ln -sf /var/log/nginx/$DATE/access.log /var/log/nginx/access.log
ln -sf /var/log/nginx/$DATE/error.log /var/log/nginx/error.log

nginx -g 'daemon off;'
