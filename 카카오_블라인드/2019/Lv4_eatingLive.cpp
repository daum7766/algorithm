#include <string>
#include <vector>
#include <algorithm>
#include <iostream>
#include <queue>

using namespace std;

int solution(vector<int> food_times, long long k) {
	long long sum = 0, before = 0;  //합과 이전값 저장용
	priority_queue<pair<int, int>> pfood_times; //우선순위 큐
	//우선순위 큐로 옮기면서 합확인(min heap을 위해 -로 반전)
	for (int i = 0; i < food_times.size(); i++) {
		sum += food_times[i];
		pfood_times.push(make_pair(-food_times[i], (i + 1)));
	}//총시간이 K보다 적거나 같다면 -1을 리턴
	if (sum <= k)	return -1;
	//작은 음식만큼 시간을 소요하는데 걸리는 시간은 (현재 제일작은 음식 - 이전음식값 * 총 음식개수) 이다.
	//이 시간만큼 K를빼주고 음식도 뺀다.(계산할때 -넣었어서 뒤집는다)
	while ((-pfood_times.top().first - before) * pfood_times.size() <= k) {
		k -= (-pfood_times.top().first - before) * pfood_times.size();
		before = -pfood_times.top().first;
		pfood_times.pop();
	}//반복문이 끝났다면 순서대로 파악한다.
	vector<pair<int, int>> ftimes;
	//편한 파악을 위해 vector로 옮긴다.
	while (!pfood_times.empty()) {
		//정렬 비교함수를 만들기 귀찮으니까 pair를 뒤집어준다.
		ftimes.push_back(make_pair(pfood_times.top().second, -pfood_times.top().first));
		pfood_times.pop();
	}
	//원래 순서대로 정렬한다.
	sort(ftimes.begin(), ftimes.end());
	//나머지 연산으로 위치찾고 반환
	return ftimes[k % ftimes.size()].first;
}


void print(vector<int> food_times, long long k, int answer) {
	int t = solution(food_times, k);
	if (answer == t)
		cout << "정답" << endl;
	else
		cout << "틀림" << endl;
}

int main() {
	print({ 3,1,2 }, 5, 1);
	print({ 8,6,4 }, 15, 2);
	print({ 946, 314, 757, 322, 559, 647, 983, 482, 145 }, 1833, 1);

	return 0;
}
