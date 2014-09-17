#!/bin/bash

# Upgrades legacy {% url url_name %} style template tag to Django 1.5+
# style {% url 'url_name' %}

# TODO allow for checking only without replacing

usage()
{
cat << EOF
usage: $0 options

This scripts ensures the Django 'url' tag quotes URL names.

OPTIONS:
   -h      Show this message
   -d      Directory to start searching from
   -f      File extension to search
   -e      Edit files in place
EOF
}


DIR="."
EXT="html"
EDIT=0
while getopts "hd:f:e" OPTION
do
     case $OPTION in
         h)
             usage
             exit 1
             ;;
         d)
             DIR=$OPTARG
             ;;
         f)
             EXT=$OPTARG
             ;;
         e)
             EDIT=1
             ;;
         ?)
             usage
             exit 1
             ;;
     esac
done


if [ $EDIT -eq 1 ]
then
  find $DIR -type f -name "*.$EXT" -print0 | xargs -0 sed -i -r -e "s#\{% url ([a-zA-Z0-9_.:-]+)#\{% url '\1'#g"
else
  grep -rn --include="*.$EXT" "\{% url [^']" $DIR
  RETVAL=$?
  if [ $RETVAL -eq 1 ]
  then
    EXITCODE=0
  else
    EXITCODE=1
  fi
  exit $EXITCODE
fi