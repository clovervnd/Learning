#include <iostream>

using namespace std;

class B;

class A{
	private:
		int adata;
	public:
		A(int _data)
		{
			adata = _data;
		}
		void ShowData(B b);
		friend class B;
};

class B{
	private :
		int bdata;
	public: 
		B(int _data){
			bdata = _data;
		}
		void ShowData(A a)
		{
			cout << "a.data: " << a.adata <<endl;
		}
		friend class A;
};

void A::ShowData(B b)
{
	cout << "b.data: " <<b.bdata<<endl; 
}

int main(){
	A a(10);
	B b(20);
	
	a.ShowData(b);
	b.ShowData(a);
	return 0;
}
