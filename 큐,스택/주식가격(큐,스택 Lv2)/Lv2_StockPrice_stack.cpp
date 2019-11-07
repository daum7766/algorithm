#include <vector>

using namespace std;

vector<int> solution(vector<int> prices) {
	vector<int> answer;
	for (int i = 0; i < prices.size() - 1; i++)
	{
		int count = 0;
		for (int j = i + 1; j < prices.size(); j++)
		{
			//다음거보다 가격이 떨어지지 않았따면
			if (prices.at(i) <= prices.at(j))
			{
				count++;
			}
			else//가격이 떨어졌다면
			{
				count++;
				break;
			}
		}
		answer.push_back(count);
	}
	//제일 마지막꺼 처리
	answer.push_back(0);

	return answer;
}