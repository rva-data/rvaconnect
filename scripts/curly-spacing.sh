#!/bin/bash

# TODO account for MORE than one space

usage()
{
cat << EOF
usage: $0 options

This scripts ensures proper spacing around template tag delimiters.

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
  find $DIR -type f -name "*.$EXT" -print0 | xargs -0 sed -i -r -e "s#\{%([a-zA-Z0-9_.:-]+)#\{% \1#g;s#([a-zA-Z0-9_.:-]+)%\}#\1 %\}#g;s#\{\{([a-zA-Z0-9_.:-]+)#\{\{ \1#g;s#([a-zA-Z0-9_.:-]+)\}\}#\1 \}\}#g"
else
  grep -rn --include="*.$EXT" "\{%\S\|\S%\}\|\{{\S\|\S\}}" $DIR
  RETVAL=$?
  if [ $RETVAL -eq 1 ]
  then
    EXITCODE=0
  else
    EXITCODE=1
  fi
  exit $EXITCODE
fi