#!/bin/bash

eval $(/opt/elasticbeanstalk/bin/get-config environment | jq -r 'to_entries[] | "\(.key)=\(.value)"')