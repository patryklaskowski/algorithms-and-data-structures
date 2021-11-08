#!/bin/bash

python3 -m unittest -v

ERR_CODE=$?

if [[ $ERR_CODE != 0 ]]
then
  exit 1
fi
