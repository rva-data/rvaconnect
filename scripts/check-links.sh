#!/usr/bin/env bash

# This is just a slight wrapper around pylinkvalidate.py


usage()
{
cat << EOF
usage: $0 <environment_name>

This script wraps pylinkvalidate.py to check for broken links (a, img, etc) in
the remote environments.

Specify an active environment name, either 'staging' or 'production'
EOF
}

LOGNAME="crawl-$(date +%Y-%m-%d).log"

case "$1" in
  staging)
    HOST=staging.rvaconnect.com
    pylinkvalidate.py --progress --test-outside --parser=lxml --accepted-hosts=$HOST --username=username --password=password --output="local_data/staging-$LOGNAME" http://$HOST
    ;;
  production)
    HOST=www.rvaconnect.com
    pylinkvalidate.py --progress --test-outside --parser=lxml --accepted-hosts=$HOST --output="local_data/staging-$LOGNAME" http://$HOST
    ;;
  *)
    usage
    exit
    ;;
esac