#include <string>
#include <vector>
#include <iostream>

using namespace std;


vector<int> solution(vector<int> prices) {
	vector<int> answer;
	//마지막을 제외하고 순회(마지막은 가격변동이 없기때문)
	for (int i = 0; i < prices.size() - 1; i++) {
		int count = 0;
		//자기보다 뒤에를 순회하면서 자기보다 가격이 낮으면 반복문을 멈춤
		for (int j = i + 1; j < prices.size(); j++) {
			count++;
			if (prices.at(i) > prices.at(j))
				break;
		}
		//지속된 시간입력
		answer.push_back(count);
	}
	//제일 마지막꺼 처리
	answer.push_back(0);

	return answer;
}

void print(vector<int> prices, vector<int> answer) {
	vector<int> t = solution(prices);
	//cout << t << " , ";
	if (answer == t)
		cout << "정답" << endl;
	else
		cout << "틀림" << endl;
}

int main() {
	print({ 1,2,3,2,3 }, { 4,3,1,1,0 });
	return 0;
}
