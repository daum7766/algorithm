#include <iostream>
#include <vector>
#include <queue>

using namespace std;

int solution(int stock, vector<int> dates, vector<int> supplies, int k){
	//공급횟수
	int answer = 0;
	//우선순위큐 맥스힙
	priority_queue<int> pq;
	//현재날이 K날 보다 적을때까지 반복
	for (int day = 0, j = 0; day < k; day++){
		//공급 가능한 날이 있고 그날이 이미 지났다면
		if (dates.size() > j && dates.at(j) <= day){
			//우선순위 큐에 넣음
			pq.push(supplies.at(j));
			j++;
		}
		//현재 밀가루를 다썻다면
		if (!stock){
			//공급 받을수있는 최대량을 공급받음
			stock += pq.top();
			//우선순위 큐에서 제거
			pq.pop();
			//공급받은 횟수증가
			answer++;
		}
		//밀가루 사용
		stock--;
	}

	return answer;
}

void print(int stock, vector<int> dates, vector<int> supplies, int k, int answer) {
	int t = solution(stock, dates, supplies, k);
	if (t == answer)
		cout << "정답" << endl;
	else
		cout << "틀림" << endl;
}


int main(){
	print(4, { 4, 10, 15 }, {20, 5, 10}, 30, 2);
	return 0;
}