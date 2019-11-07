#include <string>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

int solution(vector<int> weight) {
	//1부터 비교를 시작
	int answer = 1;
	sort(weight.begin(), weight.end());
	/*
	ex) 백터가 {3, 1, 6, 2, 7, 30, 1}이라고 하자
	정렬후 {1, 1, 2, 3, 6, 7, 30}이 된다.
	이걸 오름차순 정렬후 앞부터 더한 값과 비교를 시작
	주의 해야 할점은 answer-1은 앞의 추로 만들수 있는 최대의 수이다.
	1,1,2,3의 추를 이용하면 7까지 모든 경우의 수를 만들 수 있다.
	4 = 2 + 1 +1
	5 = 2 + 3
	6 = 3 + 2 + 1
	7 = 3 + 2 + 1 + 1
	만약 지금까지 더한수보다 더 큰 추가 나온다면 answer는 만들 수 없는 수이다.
	*/
	for (auto w : weight) {
		if (answer < w)
			break;
		answer += w;
	}
	return answer;
}

void print(vector<int> weight, int answer)
{
	int t = solution(weight);
	cout << t << " , ";
	if (answer == t)
		cout << "정답" << endl;
	else
		cout << "틀림" << endl;
}

int main()
{
	print({ 3,1,6,2,7,30,1 }, 21);
	return 0;
}