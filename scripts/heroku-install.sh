#!/usr/bin/env bash

echo "Ensuring that you have the necessary plugins..."

heroku labs:enable pipelines
heroku plugins:install git://github.com/heroku/heroku-pipeline.git

echo "Finished!"