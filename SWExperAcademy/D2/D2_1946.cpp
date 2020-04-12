#include <iostream>
#include <vector>
#include <string>

using namespace std;
//1946 D2 간단한 압축풀기
int main() {
	//전체 반복횟수
	int len;
	cin >> len;
	for (int l = 1; l <= len; l++) {
		int num, s_cnt=0, n_count;
		string str;
		cin >> num;
		cout << "#" << l << endl;
		//A~Z까지 입력받기
		for (int i = 0; i < num; i++) {
			cin >> str >> n_count;
			//압축된 횟수만큼 반복
			for (int j = 0; j < n_count; j++) {
				//10회마다 줄내림
				if (s_cnt / 10) {
					cout << endl;
					s_cnt %= 10;
				}
				cout << str;
				s_cnt++;
			}
		}
		cout << endl;
	}
	return 0;
}