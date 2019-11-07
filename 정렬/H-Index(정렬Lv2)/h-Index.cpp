#include <string>
#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;

int solution(vector<int> citations) {
	int answer = 0;
	sort(citations.begin(), citations.end());
	//제일 큰값이 0이라면 H-index 는 0이다
	if (citations.at(citations.size() - 1) == 0)
	{
		return 0;
	}
	for (int i = citations.size() - 1, k = 0; i >= 0; i--, k++)
	{
		//h-index범위 안이라면
		if (citations.at(i) > k)
			answer = k;
		//최대값을 벗어났다면
		else
		{
			answer++;
			break;
		}
		//마지막 까지 왔다면 사이즈만큼이 h-index
		if (i == 0)
			return citations.size();
	}
	return answer;
}

int main()
{
	vector<int> a = { 3, 0, 6, 1, 5 };
	cout << solution(a) << endl;
	a = { 7 };
	cout << solution(a) << endl;
	a = { 1545, 2, 999, 790, 540, 10, 22 };
	cout << solution(a) << endl;

	return 0;
}