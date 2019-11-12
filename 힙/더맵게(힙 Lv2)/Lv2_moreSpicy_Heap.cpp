#include <iostream>
#include <vector>
#include <queue>

using namespace std;

int solution(vector<int> scoville, int K) {
	int answer = 0;
	//우선순위큐 오름차순
	priority_queue<int, vector<int>, greater<int> > pq(scoville.begin(), scoville.end());
	//음식이 최소2개이상이고 제일안매운 음식이 K보다 작을때까지만 반복
	while (pq.size() > 1 && pq.top() < K){
		int first = pq.top();
		pq.pop();
		int second = pq.top();
		pq.pop();
		//두개의 음식을 섞어서 우선순위 큐에 추가
		pq.push(first + (second * 2));
		//조합 횟수 증가
		answer++;
	}
	//모든 조합이 끝났을때 우선순위 큐의 제일 맵지 않은 음식이 K보다 작다면 -1을 리턴
	if (pq.top() < K)	return -1;
	return answer;
}

void print(vector<int> scoville, int K, int answer) {
	int t = solution(scoville, K);
	if (t == answer)
		cout << "정답" << endl;
	else
		cout << "틀림" << endl;

}

int main(){
	
	print({ 1,2,3,9,10,12 }, 4, 2);
	return 0;
}