#include <iostream>

using namespace std;

class ExConstructor
{
	public:
	ExConstructor()
	{
		cout << "ExConstructor() called!"<<endl;
	}
	ExConstructor(int a)
	{
		cout << "ExConstructor(int a) called" <<endl;
	}
	ExConstructor (int a,  int b)
	{
		cout << "ExConstructor(int a, int b) called"<<endl;
	}
};

int main(){
	ExConstructor a;
	ExConstructor b(10);
	ExConstructor c(10,20);
	return 0;
}
