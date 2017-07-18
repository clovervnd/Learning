#!/usr/local/bin/python3

for dir in *
do
count=0
touch "new_$dir"
while read line
do
if [ $count -eq 0 ]
then
echo "#!/usr/local/bin/python3" >> "new_$dir"
else
echo "$line" >> "new_$dir"
fi
let "count=$count+1"
done < $dir
done

