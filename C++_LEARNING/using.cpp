#include <iostream>

namespace A {
	void Add() {
		std::cout<<"A의 Add() 호출!\n";
	}
	void Minus() {
		std::cout<<"A의 Minus() 호출!\n";
	}
}

using namespace A;
// using namespace A::Add;

int main() {
	Add();
	Minus();
	return 0;
}

