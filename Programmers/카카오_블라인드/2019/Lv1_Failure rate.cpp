#include <string>
#include <vector>
#include <algorithm>
#include <iostream>
#include <map>

using namespace std;

bool compare(pair<int, double>& a, pair<int, double>& b) {
	if (a.second == b.second)
		return a.first < b.first;
	return a.second > b.second;
}

vector<int> solution(int N, vector<int> stages) {
	vector<int> answer;
	sort(stages.begin(), stages.end());
	vector<pair<int, double>> percent;	//각스테이지와 스테이지 실패율
	map<int, int> stagesClear;	//각 스테이지별 머무는 인원 
	int pCount = stages.size();	//스테이지 클리어 인원수
	for (int j = 0; j < stages.size(); j++)	//스테이지 클리어 인원수 분리
		stagesClear[stages[j]]++;
	for (int i = 1; i <= N; i++) {		//1스테이지부터 N스테이지까지 순회
		if (!pCount || !stagesClear[i])//스테이지와 못깬인원/총 인원으로 나눔
			percent.push_back({ i, 0 });
		else
			percent.push_back({ i, (double)stagesClear[i] / pCount });
		pCount -= stagesClear[i];		//깨지못한 인원들만큼 빼기
	}
	sort(percent.begin(), percent.end(), compare);//내림차순으로 정렬
	for (auto p : percent)		//정답에 옮기기
		answer.push_back(p.first);
	return answer;
}

void print(int N, vector<int> stages, vector<int> answer) {
	vector<int> t = solution(N, stages);
	if (answer == t)
		cout << "정답" << endl;
	else
		cout << "틀림" << endl;
}

int main() {

	print(4, { 2,2,2,2,2 }, { 2,1,3,4 });
	print(4, { 4,4,4,4,4 }, { 4,1,2,3 });
	print(5, { 2,1,2,6,2,4,3,3 }, { 3,4,2,1,5 });
	return 0;
}
