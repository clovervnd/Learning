# include <iostream>
using namespace std;

class memInit{
	private:
		int num1;
		int num2;
		char * name;
		// string의 경우 strcpy를 이용해서 카피해주는게 메모리 관리 차원에서 더 좋을것같음
	public:
		memInit(int _num1, int _num2, char* _name) : num1(_num1), num2(_num2), name(_name){}
		void ShowInfo()
		{
			cout << "num1: " << num1 << ", num2: " << num2 << ", name: "<< name << endl;
		}
};

int main()
{
	memInit mi (50, 70, "자영이");
	mi.ShowInfo();
	return 0; 
}

