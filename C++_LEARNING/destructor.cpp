#include <iostream>

using namespace std;

class ExConstructor
{
public:
	ExConstructor()
	{
		cout << "ExConstructor() called!" << endl;
	}
	~ExConstructor()
	{
		cout << "~ExConstructor() called!" << endl;
	}
};

int main(){
	ExConstructor a;
	return 0;
}

