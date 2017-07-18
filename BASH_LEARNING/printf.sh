E_BADDIR=65

var=nonexistent_directory

error()
{
  printf "$@" >&2
  # 인자로 넘어온 위치 매개변수를 형식화해서 표준에러로 출력
  echo
  exit $E_BADDIR
}

cd $var || error $"%s 로 바꿀 수 없습니다." "$var"

# Thanks, S.C.
