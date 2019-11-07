#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;
/*
	DFS 사용
*/

void dfs(vector<int>& numbers, int& answer, int target, int count = 0, int sum = 0){
	int s = sum, c = count;
	//마지막까지 순회했다면
	if (c == numbers.size() - 1) {
		//지금까지 더한값에 마지막 원소를 더할때 타겟과 같다면 카운트 증가
		if (target == s + numbers[c])
			answer++;
		//지금까지 더한값에 마지막 원소를 뺄때 타겟과 같다면 카운트 증가
		if (target == s - numbers[c])
			answer++;
		return;
	}
	//최대깊이까지 가지않았다면 더하거나 뺀상태로 탐색
	dfs(numbers, answer, target, count + 1, s + numbers[c]);
	dfs(numbers, answer, target, count + 1, s - numbers[c]);
}


int solution(vector<int> numbers, int target) {
	int answer = 0;
	dfs(numbers, answer, target);
	return answer;
}

void print(vector<int> numbers, int target, int answer)
{
	int t = solution(numbers, target);
	cout << t << " , ";
	if (t == answer)
		cout << "정답" << endl;
	else
		cout << "틀림" << endl;
}

int main() {

	print({ 1,1,1,1,1 }, 3, 5);

	return 0;
}