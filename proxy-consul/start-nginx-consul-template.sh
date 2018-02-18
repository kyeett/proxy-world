#!/bin/bash
nginx
echo -e "\n** nginx startedn\n"
echo -e "** starting consul-template\n"
/bin/consul-template -template /tmp/example.ctmpl:/etc/nginx/nginx.conf:'nginx -s reload' $@