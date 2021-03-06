#include <iostream>
#include <cstring>

using namespace std;

class Student
{
private:
	char name[10];
	int age;
	int studentID;
public:
	Student(char *_name, int _age, int _studentID) : age(_age), studentID(_studentID)
	{
		strcpy(name, _name);
	}
	void SetInfo (char* _name, int _age, int _studentID)
	{
		age = _age;
		studentID = _studentID;
		strcpy(name, _name);
	}
	void GetInfo()
	{
		cout << "이름: " << name << endl;
		cout << "나이: " << age << endl;
		cout << "학번: " << studentID << endl;
	}
	~Student() { cout << "소멸자 호출!" <<endl;}
};

int main()
{
	Student * student[3];
	char name[10];
	int age, studentID;
	
	for (int i=0; i<3; i++) {
		cin >> name >> age >> studentID;
		student [i] = new Student (name, age, studentID);
	}
	for (int i =0; i<3; i++) {
		student[i]->GetInfo();
	}
	delete student[0];
	delete student[1];
	delete student[2];

}
