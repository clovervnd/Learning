#!/bin/bash

for dir in *
do
	count=0
	while read line
	do
		if [ $count -eq 0]
		then
			echo "\/#!\/usr\/local\/bin\/python3" >> "$dir_old"
		else
			echo $line >> "$dir_old"
		fi
	done < $dir
done

