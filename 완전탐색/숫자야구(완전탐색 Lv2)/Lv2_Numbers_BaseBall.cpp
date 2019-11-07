#include <iostream>
#include <vector>
#include <string>

using namespace std;

int solution(vector<vector<int>> baseball) {
	vector<string> a;
	//할수 있는 경우의 수 추가
	for (int i = 123; i <= 987; i++) {
		string temp{ to_string(i) };
		if (temp[0] == temp[1] || temp[1] == temp[2] || temp[2] == temp[0] || temp[0] == '0' || temp[1] == '0' || temp[2] == '0')
			continue;
		a.push_back(temp);
	}
	//경우의 수 확인하기
	for (auto b : baseball) {
		string temp = to_string(b.at(0));
		for (int i = a.size() - 1; i >= 0; i--) {
			int strike = 0, ball = 0;
			for (int j = 0; j < 3; j++) {
				//스트라이크 수 체크
				if (temp[j] == a.at(i)[j])
					strike++;
				//볼 수 체크
				if (temp[j] == a.at(i)[(j + 1) % 3] || temp[j] == a.at(i)[(j + 2) % 3])
					ball++;
			}
			//스트라이크나 볼의 수가 맞지않는다면 경우의 수에서 제거
			if (strike != b.at(1) || ball != b.at(2))
				a.erase(a.begin() + i);
		}
	}
	//남은 경우의 수 반환
	return a.size();
}

int main() {

	vector<vector<int>> baseball{ {123, 1, 1}, {356, 1, 0}, {327, 2, 0}, {489, 0, 1} };
	cout << solution(baseball) << endl;
	return 0;
}