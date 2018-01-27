#!/bin/bash

NEW_NAME=`python getArXivName.py $1`

mv $1 "${NEW_NAME}"