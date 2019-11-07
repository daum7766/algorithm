#include <vector>
#include <iostream>
#include <queue>
#include <algorithm>

using namespace std;

bool compare(vector<int> a, vector<int> b) {
	return a.at(0) < b.at(0);
}

struct cmp {
	bool operator()(vector<int> a, vector<int> b) {
		return a.at(1) > b.at(1);
	}
};

int solution(vector<vector<int>> jobs) {
	int answer = 0;	//결과 저장용 변수
	int j = 0;	//인덱스 관리용
	int time = 0;	//시간 체크용
	sort(jobs.begin(), jobs.end(), compare);
	priority_queue<vector<int>, vector<vector<int>>, cmp> pq; //우선순위 큐 min heap
	//대기열이 없고 우선순위 큐가 빌때까지 반복
	while (j < jobs.size() || !pq.empty()) {
		//들어올 대기열이 남아있고, 들어올 대기열이 현재시간보다 작다면
		if (jobs.size() > j && time >= jobs.at(j).at(0)) {
			//우선순위 큐에 추가
			pq.push(jobs.at(j));
			//인덱스 증가
			j++;
			//같은시간대에 다른작업이 더들어왔을 수 있으므로 다시 확인
			continue;
		}
		//큐가 비어있지 않다면
		if (!pq.empty()) {
			//시간에 이작업이 끝날때까지 걸리는 시간만큼 추가
			time += pq.top().at(1);
			//작업시간에 대기 시간만큼 추가(현재시간 - 들어온 시간)
			answer += time - pq.top().at(0);
			//작업이 끝났으므로 우선순위 큐에서 제거
			pq.pop();
		}
		else {//큐가 비어있다면
			time++;//시간증가
		}
	}
	return answer / jobs.size();//평균을 구해야하므로 총작업한 개수로 나눠줌
}

int main()
{
	//int ajobs[][2] = { {0, 3}, {1, 9}, {2, 6}};
	int ajobs[][2] = { {1, 4}, {1, 3}, {1, 5}, {2, 4}, {2, 3} ,{3, 1} };
	vector<vector<int>> jobs;
	for (int i = 0; i < 6; i++)
	{
		vector<int> temp;
		temp.push_back(ajobs[i][0]);
		temp.push_back(ajobs[i][1]);
		jobs.push_back(temp);
	}
	cout << solution(jobs) << endl;
	return 0;
}