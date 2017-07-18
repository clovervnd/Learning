#include <iostream>

using namespace std;

class Parent {
public :
	// pure virtual function declaration
	virtual void func() = 0;
};

class Child : public Parent {
public :
	virtual void func() { cout << "자식 클래스의 func 함수 호출!" <<endl; }
};

int main()
{
	Parent *p;

	p = new Child;
	p->func();
	return 0;
}


