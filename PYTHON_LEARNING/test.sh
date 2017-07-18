#!/bin/bash

count=0
while [ $count -le 10 ]
do
	touch node$count
	let "count=$count+1"
done
