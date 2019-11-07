#include <string>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

int solution(vector<vector<int>> routes) {
	//기본 카메라 1대
	int answer = 1;
	//들어온 리스트 정렬
	sort(routes.begin(), routes.end());
	//비교를 위해 처음차가 나가는 부분 체크
	int temp = routes.at(0).at(1);
	//리스트 순회하기
	for (auto a : routes) {
		cout << a.at(0) << " , " << a.at(1) << endl;
		//현재 차가 나가는 부분보다 뒤에 차가 들어온다면
		if (temp < a.at(0)) {
			//카메라 설치
			answer++;
			//나가는 부분 정정
			temp = a.at(1);
		}
		//현재 차보다 뒤차가 먼저나가면 
		if (temp >= a.at(1))
			temp = a.at(1);// 나가는 부분을 뒷차로 수정
	}
	return answer;
}

void print(vector<vector<int>> routes, int answer)
{
	int t = solution(routes);
	cout << t << " , ";
	if (t == answer)
		cout << "정답" << endl;
	else
		cout << "틀림" << endl;

}


int main()
{
	print({ {-20,15}, {-14, -5}, {-18, -13}, {-5, -3} }, 2);
	print({ {-2, -1}, {1, 2}, {-3, 0} }, 2);
	print({ {0, 0} }, 1);
	print({ {0, 1}, {0, 1}, {1, 2} }, 1);
	print({ {0, 1}, {2, 3}, {4, 5}, {6, 7} }, 4);
	print({ {-20, 15}, {-14, -5}, {-18, -13}, {-5, -3} }, 2);
	print({ {-20, 15}, {-20, -15}, {-14, -5}, {-18, -13}, {-5, -3} }, 2);

	return 0;
}