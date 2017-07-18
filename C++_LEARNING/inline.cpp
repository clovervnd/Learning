#include <iostream>
#define PI 3.141592


// inline function does the similar work as pre-processors (#define, #if) in C++

inline int CU(int x)
{
	return x*x*x;
}

using namespace std;

int main()
{
	cout << PI << endl;
	cout << CU(7) << endl;
	return 0;
}

