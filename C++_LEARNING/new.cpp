#include <iostream>

using namespace std;

int main(){

	int StudentNum, TotalScore = 0;
	int * StudentScore;
	int i;

	cout<< "학생 수를 입력하세요: ";
	cin>> StudentNum;
	StudentScore = new int[StudentNum];

	for ( i=0; i<StudentNum; i++) {
		cout<< i+1 << "번 학생의 점수: ";
		cin>>StudentScore[i];
		TotalScore += StudentScore[i];
	}

	cout << "모든 학생의 평균: " <<TotalScore/StudentNum <<endl;
	delete []StudentScore;
	return 0;
}
