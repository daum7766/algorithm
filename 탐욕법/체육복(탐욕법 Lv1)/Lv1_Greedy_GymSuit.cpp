#include <vector>
#include <iostream>

using namespace std;

int solution(int n, vector<int> lost, vector<int> reserve) {
	int answer = 0;
	//총 인원수만큼 벡터를 생성하고 체육복갯수 1로 설정
	vector<int> check(n, 1);
	//체육복을 잃어버린 사람은 1개 마이너스
	for (auto l : lost)		check.at(l - 1)--;
	//체육복을 여분으로 가져왔다면 1개 플러스
	for (auto r : reserve)		check.at(r - 1)++;
	//처음부터 돌면서 순회하기
	for (int i = 0; i < check.size(); i++) {
		//체육복이 0개라면
		if (check.at(i) == 0) {
			//앞의 사람이 여분이 있나 확인하고 있다면 빌리기
			if (i != check.size() - 1 && check.at(i + 1) == 2) {
				check.at(i + 1)--;
				check.at(i)++;
			}
			//뒤에 사람이 여분이 있나 확인하고 있다면 빌리기
			else if (i != 0 && check.at(i - 1) == 2) {
				check.at(i - 1)--;
				check.at(i)++;
			}
		}
	}
	//체육복이 몇명이 있나 체크하기
	for (auto a : check)
		if (a != 0)	answer++;

	return answer;
}

void print(int n, vector<int> lost, vector<int> reserve)
{
	cout << solution(n, lost, reserve) << endl;
}


int main() {

	print(7, { 2, 3, 4 }, { 1, 2, 3, 6 });
	print(5, { 2, 4 }, { 1, 3, 5 });
	print(5, { 2, 4 }, { 3 });
	print(3, { 3 }, { 1 });

	return 0;
}