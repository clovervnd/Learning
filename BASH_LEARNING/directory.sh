#!/bin/bash

dir1=/usr/local
dir2=/var/spool

pushd $dir1
# 자동으로 'dirs'를 실행합니다(디렉토리 스택의 내용을 표준출력으로 뿌림).
echo "Now in directory `pwd`." # 역따옴표(backquote)를 건 'pwd'.

# 'dir1'에서 아무 일이나 하고,
pushd $dir2
echo "지금은 `pwd` 디렉토리에 있습니다."

# 'dir2'에서 아무 일이나 한 다음,
echo "DIRSTACK 배열의 top 항목은 $DIRSTACK 입니다."
popd
echo "이제 `pwd` 디렉토리로 돌아왔습니다."

# 'dir1'에서 아무 일이나 하세요.
popd
echo "이제 원래의 `pwd` 디렉토리로 돌아왔습니다."

exit 0
