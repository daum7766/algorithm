#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;
//D2 1974 스도쿠 배열 검증
int list[9][9];
//사각형 검사하는 함수
int nextCheck() {
	//제일윗줄부터 오른쪽으로 진행하며 검사
	for (int i = 0; i < 9; i += 3) {
		for (int j = 0; j < 9; j += 3) {
			int sum[10]{ 0 };
			//현재 i와j위치에서 +3개씩 검사
			for (int k = i; k < i + 3; k++) {
				for (int y = j; y < j + 3; y++) {
					if (sum[list[k][y]])
						return 0;
					sum[list[k][y]]++;
				}
			}
		}
	}
	return 1;
}

int solution() {
	//스도쿠 데이터를 입력받음
	for (int i = 0; i < 9; i++) {
		for (int j = 0; j < 9; j++)
			cin >> list[i][j];
	}
	//가로세로를 돌면서 중복이 있는지 체크
	for (int i = 0; i < 9; i++) {
		int sum1[10]{ 0 }, sum2[10]{ 0 };
		for (int j = 0; j < 9; j++) {
			if (sum1[list[i][j]] || sum2[list[j][i]])
				return 0;
			sum1[list[i][j]]++;
			sum2[list[j][i]]++;
		}
	}
	//가로세로에 이상이없다면 3칸짜리 삼각형 검사
	return nextCheck();
}

int main() {
	int length;
	cin >> length;
	for (int l = 1; l <= length; l++)
		cout << "#" << l << " " << solution() << endl;
	return 0;
}