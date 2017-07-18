#include <iostream>

using namespace std;
/* 
struct student{
	int id;
	char *name;
	float percentage; 

	void Show()	{
		cout << "아이디: " << id << endl;
		cout << "이름: " << name << endl;
		cout << "백분율: " << percentage << endl;
	}
};
*/

struct student{
	int id;
	char *name;
	float percentage;
	
	void Show();
};

void student::Show(){
	cout << "아이디: "<< id << endl;
	cout << "이름: "<< name<< endl;
	cout << "백분율: "<< percentage<< endl;
}

int main (){
	student s = {1, "김철수", 90.5};

	s.Show();
	return 0;
}
