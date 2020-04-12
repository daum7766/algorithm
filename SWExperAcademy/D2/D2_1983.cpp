#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

int main() {
	//총 반복 횟수
	int length;
	//성적에 따른 등급
	string answer[10]{ "A+", "A0", "A-" , "B+", "B0", "B-", "C+", "C0", "C-", "D0" };
	cin >> length;
	for (int i = 1; i <= length; i++) {
		//성적 ,총학생수, 학생번호
		int grade[3], n, k;
		//학생 번호하고 성적을 저장하기위한 vector
		vector<pair<double, int> > student;
		cin >> n >> k;
		//성적 입력받기
		for (int z = 0; z < n; z++) {
			for (int j = 0; j < 3; j++)
				cin >> grade[j];
			//성적에 따른 총성적과 학생번호 등록
			student.push_back(make_pair(grade[0] * 0.35 + grade[1] * 0.45 + grade[2] * 0.2, z));
		}
		//정렬하기(내림차순 정렬이 Gcc 4.8.5버전에서 되지않아서 reverse사용)
		sort(student.begin(), student.end());
		reverse(student.begin(), student.end());
		for (int j = 0; j < student.size(); j++) {
			if (student[j].second == k - 1)//그냥 나누면 0~1사이이기때문에 *10을해서 나눠준다.
				cout << "#" << i << " " << answer[(j * 10) / student.size()] << endl;
		}
	}
	return 0;
}