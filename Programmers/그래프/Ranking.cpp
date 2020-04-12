#include <string>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

int solution(int n, vector<vector<int>> results) {
	int answer = 0;
	vector<vector<bool>> graph(n + 1, vector<bool>(n + 1, false));
	//승리한 경우 추가
	for (auto r : results) 	graph[r[0]][r[1]] = true;
	//자신한테 진 사람이 승리한경우는 자신도 승리로 처리하기
	//i 거쳐가는 노드
	for (size_t i = 1; i <= n; i++) {
		//j 출발노드
		for (size_t j = 1; j <= n; j++) {
			//k 도착노드
			for (size_t k = 1; k <= n; k++) {
				if (graph[i][j] && graph[j][k]) {
					graph[i][k] = true;
				}
			}
		}
	}
	for (size_t i = 1; i <= n; i++) {
		int count = 0;
		//내가 이겼거나 상대방이 이긴경우 판단이 가능하므로 count증가
		for (size_t j = 1; j <= n; j++) {
			if (graph[i][j] || graph[j][i])	count++;
		}
		//판단이 가능한판수가 총인원-1이라면 확인이 가능하므로 answer증가
		if (count == n - 1)	answer++;
	}
	return answer;
}

void print(int n, vector<vector<int>> results, int answer) {
	int t = solution(n, results);
	if (t == answer)		cout << "정답" << endl;
	else		cout << "틀림" << endl;
}

int main() {
	print(5, { {4, 3}, {4, 2}, {3, 2}, {1, 2},{2, 5} }, 2);
	return 0;
}