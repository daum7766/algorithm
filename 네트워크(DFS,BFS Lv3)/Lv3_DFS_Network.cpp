#include <iostream>
#include <vector>
#include <string>
using namespace std;

bool dfs(vector<vector<int>>& computers, int n) {
	//이미 순회한 노드라면 리턴(재귀함수 탈출조건)
	if (!computers[n][n])
		return false;
	//순회했다고 변경하기
	computers[n][n] = 0;
	//노드수만큼 반복
	for (int i = 0; i < computers.size(); i++) {
		//연결된 노드가 있다면 재귀
		if (computers[n][i])
			dfs(computers, i);
	}
	return true;
}


int solution(int n, vector<vector<int>> computers) {
	int answer = 0;
	for (int i = 0; i < n; i++) {
		//순회하지 않은 노드라면 dfs탐색후 answer증가
		if (computers[i][i] && dfs(computers, i))
			answer++;
	}
	return answer;
}

void print(int n, vector<vector<int>> computers, int answer)
{
	int t = solution(n, computers);
	cout << t << " , ";
	if (t == answer)
		cout << "정답" << endl;
	else
		cout << "틀림" << endl;
}

int main() {

	print(3, { {1,1,0}, {1,1,0},{0,0,1} }, 2);
	print(3, { {1,1,0}, {1,1,1},{0,1,1} }, 1);

	return 0;
}