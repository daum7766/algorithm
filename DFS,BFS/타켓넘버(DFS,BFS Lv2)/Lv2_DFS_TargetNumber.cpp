#include <iostream>
#include <vector>
#include <string>
using namespace std;
/*
	DFS 사용
*/
//벡터, 정답횟수, 찾아야 하는 숫자, 들어간 깊이, 현재까지 합
void dfs(vector<int>& numbers, int& answer, int target, int count = 0, int sum = 0){
	//마지막까지 순회했다면
	if (count == numbers.size() - 1) {
		//지금까지 더한값에 마지막 원소를 더할때 타겟과 같다면 카운트 증가
		if (target == sum + numbers[count])		answer++;
		//지금까지 더한값에 마지막 원소를 뺄때 타겟과 같다면 카운트 증가
		if (target == sum - numbers[count])		answer++;
		return;
	}
	//최대깊이까지 가지않았다면 더하거나 뺀상태로 탐색
	dfs(numbers, answer, target, count + 1, sum + numbers[count]);
	dfs(numbers, answer, target, count + 1, sum - numbers[count]);
}


int solution(vector<int> numbers, int target) {
	int answer = 0;
	dfs(numbers, answer, target);
	return answer;
}

void print(vector<int> numbers, int target, int answer){
	int t = solution(numbers, target);
	if (t == answer)	cout << "정답" << endl;
	else	cout << "틀림" << endl;
}

int main() {
	print({ 1,1,1,1,1 }, 3, 5);
	return 0;
}