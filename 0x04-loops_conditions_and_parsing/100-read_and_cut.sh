#!/bin/bash env
# This script read and print the content of /etc/passwd

file='/etc/passwd'

while read line; do

	echo "$line"

done < $file