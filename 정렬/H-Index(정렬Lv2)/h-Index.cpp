#include <string>
#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;

int solution(vector<int> citations) {
	int answer = 0;
	sort(citations.begin(), citations.end());
	//제일 큰값이 0이라면 H-index 는 0이다
	if (!citations.at(citations.size() - 1))
		return 0;
	for (int i = citations.size() - 1, k = 0; i >= 0; i--, k++)	{
		//h-index범위 안이라면
		if (citations.at(i) > k)
			answer = k;
		//최대값을 벗어났다면
		else{
			answer++;
			break;
		}
		//마지막 까지 왔다면 사이즈만큼이 h-index
		if (i == 0)		return citations.size();
	}
	return answer;
}

void print(vector<int> citations, int answer) {
	int t = solution(citations);
	if (t == answer)
		cout << "정답" << endl;
	else
		cout << "틀림" << endl;
}

int main(){
	print({ 3, 0, 6, 1, 5 }, 3);
	print({ 7 },1);
	print({ 1545, 2, 999, 790, 540, 10, 22 }, 6);
	print({22, 47}, 2);
	print({2, 7, 5}, 2);
	print({4, 3, 3, 3, 3}, 3);
	print({10, 50, 100}, 3);
	print({1, 7, 0, 1, 6, 4}, 3);
	print({0}, 0);
	return 0;
}