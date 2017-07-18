#include <iostream>

using namespace std;

class Parent {
public:
	// C++에서는 컴파일러가 실제로 가리키는 객체의 자료형을 기준을 화는게 아닌,
	// 포인터 변수의 자료형을 기준으로 판단한다.
	// virtual 키워드를 이용하면 실제로 가리키는  객체에 따라 실행된느 코드가 달라진다.
	virtual void func() { cout << "부모 클래스의 func 함수 호출!" << endl; }
};

class Child : public Parent {
public:
	virtual void func() { cout << "자식 클래스의 func 함수 호출!"<< endl; }
};

int main() 
{
	Parent P, *pP;
	Child C;

	pP=&P;
	pP->func();
	pP=&C;
	pP->func();
	return 0;
}
