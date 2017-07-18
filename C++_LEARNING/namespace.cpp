#include <iostream>

namespace A {
	void Add() {
		std::cout<<"A의 Add() 호출!"<<std::endl;
	}
}

namespace B {
	void Add() {
		std::cout<<"B의 Add() 호출!"<<std::endl;
	}
}

int main(){
	A::Add();
	B::Add();
	return 0;
}

