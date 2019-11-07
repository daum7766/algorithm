#include <iostream>
#include <vector>
#include <queue>

using namespace std;

vector<int> solution(vector<int> progresses, vector<int> speeds) {
	vector<int> answer;
	//현재 진척도
	queue<int> current;
	//큐에 옮기기
	for (auto p : progresses)
		current.push(p);
	while (!current.empty()) {
		//진척도 추가
		for (int i = 0; i < current.size(); i++) {
			int p = current.front();
			current.pop();
			current.push(p + speeds.at(i));
		}
		int count = 0;
		//큐 내부검사
		while (true) {
			//진척도가 100퍼센트 이상이라면 큐에서 제거하고 카운트 증가
			if (current.size() > 0 && current.front() >= 100) {
				current.pop();
				speeds.erase(speeds.begin());
				count++;
				continue;
			}
			break;
		}
		//카운트가 한개이상 올라갔다면
		//정답리스트에 몇개가 배포되는지 추가
		if (count > 0)
			answer.push_back(count);
	}
	return answer;
}

int main()
{
	vector<int> progresses = { 93, 30, 55 };
	vector<int> speeds = { 1, 30, 5 };
	vector<int> result = solution(progresses, speeds);
	for (auto t : result)
	{
		cout << t << endl;
	}
	return 0;
}