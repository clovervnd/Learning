
#!/bin/bash

# 현재 디렉토리에 /var/log/messages 의 끝 부분을 포함하는 로그 파일을 만들기

# 주의: 일반 사용자도 이 스크립트를 쓰게 하려면 
#       루트로 chmod 644 /var/log/messages 라고 해서
#       누구나 /var/log/messages 를 읽을 수 있게 해야 됩니다.

LINES=5

( date; uname -a ) >>logfile
# 시간과 머신 이름
echo --------------------------------------------------------------------- >>logfile
tail -$LINES /var/log/messages | xargs |  fmt -s >>logfile
echo >>logfile
echo >>logfile

exit 0
