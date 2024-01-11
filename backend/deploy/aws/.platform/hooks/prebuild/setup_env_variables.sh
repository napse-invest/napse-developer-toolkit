#!/bin/bash

eval $(/opt/elasticbeanstalk/bin/get-config environment | jq -r 'to_entries[] | "\(.key)=\(.value)"')
/opt/elasticbeanstalk/bin/get-config environment
export NAPSE_API_DOMAIN=napse-env.eba-vm2tsihk.eu-west-3.elasticbeanstalk.com
