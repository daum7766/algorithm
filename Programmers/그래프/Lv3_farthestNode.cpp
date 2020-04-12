#include <string>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

void bfs(int current, vector<vector<bool>>& graph, vector<int>& distance, vector<int> queue) {
	//임시큐
	vector<int> m_queue;
	//인자값으로 넘어온 큐가 빌때까지 반복
	while (!queue.empty()) {
		//연결되어있는 그래프를 확인한다.
		for (size_t i = 1; i < graph.size(); i++) {
			//큐에 들어있는 노드와 연결이 되어있어야하고, 거리설정이 안되있어야한다.
			if (graph[queue[0]][i] && !distance[i]) {
				//임시큐에 넣고 거리를 넣어준다.
				m_queue.push_back(i);
				distance[i] = current;
			}
		}
		//큐에있는 데이터 pop
		queue.erase(queue.begin());
	}
	//임시큐가 비어있지 않다면 bfs 재귀
	if (!m_queue.empty())	bfs(current + 1, graph, distance, m_queue);
}

int solution(int n, vector<vector<int>> edge) {
	int answer = 0;
	//노드의 수만큼 2차원벡터를 만들고 1차원벡터는 false로 설정한다.
	vector<vector<bool>> graph(n, vector<bool>(n, false));
	//거리는 n개의 1차원벡터로 0으로 초기화
	vector<int> distance(n, 0);
	//연결되어 있는 엣지들은 true로 변경
	for (auto e : edge) {
		graph[e[0] - 1][e[1] - 1] = true;
		graph[e[1] - 1][e[0] - 1] = true;
	}
	//bfs함수 시작, 첫노드는 0으로 설정한다.
	bfs(1, graph, distance, { 0 });
	//최대거리를 구해서 최대거리와 같은수만큼 answer증가후 리턴
	int max = *max_element(distance.begin(), distance.end());
	for (auto d : distance) {
		if (d == max)	answer++;
	}
	return answer;
}

void print(int n, vector<vector<int>> edge, int answer) {
	int t = solution(n, edge);
	if (t == answer)		cout << "정답" << endl;
	else		cout << "틀림" << endl;
}

int main() {
	print(6, { {3, 6}, {4, 3}, {3, 2}, {1, 3}, {1, 2}, {2, 4}, {5, 2} }, 3);
	return 0;
}