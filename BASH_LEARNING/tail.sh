#!/bin/bash

filename=sys.log

cat /dev/null > $filename; echo "깨끗한 파일 생성."
# 존재하지 않는 파일이라면 새로 만들고,
# 길이를 0 으로 만듦.
# : > filename   이라고 해도 됩니다.

tail /var/log/messages > $filename  
# 이 명령이 제대로 동작하려면 /var/log/messages 에 아무나 읽을 수 있는 
# 퍼미션이 걸려 있어야 됩니다.

echo "$filename 은 시스템 로그의 마지막 부분을 보여줍니다."

exit 0
