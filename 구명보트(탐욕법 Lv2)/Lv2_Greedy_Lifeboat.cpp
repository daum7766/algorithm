#include <vector>
#include <iostream>
#include <string>
#include <algorithm>
#include <set>

using namespace std;


int solution(vector<int> people, int limit) {
	int answer = 0, cnt = 0;
	//뒤에와 앞에를 가르키는 인덱스
	int begin = 0, end = 1;
	//정렬하기
	sort(people.begin(), people.end());
	while (true) {
		//제일 뒤에무게를 넣기
		int first = people[people.size() - end++];
		cnt++;	//한명 뺏다고 표시
		//최대제한에 제일무거운사람을 계산했을때 제일 가벼운사람이 탈수있다면
		if (limit - first >= people[begin])
		{
			//앞사람 인덱스 증가와 보트에 탄사람 추가
			begin++;
			cnt++;
		}
		//보트 나간횟수 증가
		answer++;
		//보트를 타고 나간사람이 총인원보다 같거나 많아지면 반복문 종료
		if (cnt >= people.size())
			break;
	}
	return answer;
}


void print(vector<int> people, int limit, int answer)
{
	int t = solution(people, limit);
	cout << t << " ";
	if (t == answer)
		cout << "정답" << endl;
	else
		cout << "틀림" << endl;

}


int main() {

	print({ 70, 50, 80, 50 }, 100, 3);
	print({ 70, 80, 50 }, 100, 3);

	return 0;
}