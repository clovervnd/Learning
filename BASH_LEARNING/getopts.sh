while getopts ":abcde:fg" Option
# 초기 선언.
# a, b, c, d, e, f, g 옵션(플래그)만 지원.
# 'e' 뒤의 :로 'e' 옵션에는 인자가 있어야 된다는 것을 나타냄
do
  case $Option in
    a ) # 'a'일 경우 할 일.
    b ) # 'b'일 경우 할 일.
    ...
    e)  # 'e'일 경우 할 일, $OPTARG 로 'e' 뒤에 따라오는 해당 인자를 처리.
    ...
    g ) # 'g'일 경우 할 일.
  esac
done
shift $(($OPTIND - 1))
# 인자 포인터를 다음으로 이동.

# 보이는 것처럼 그렇게 복잡하지는 않습니다. <씨익>.
	      
