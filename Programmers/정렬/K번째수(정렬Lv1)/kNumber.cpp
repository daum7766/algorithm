#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

vector<int> solution(vector<int> array1, vector<vector<int>> commands) {
	vector<int> answer;
	//반환되야되는 세트동안 반복
	for (int i = 0; i < commands.size(); i++){
		//임시 벡터 생성
		vector<int> temp;
		//필요한 부분만 임시벡터에 넣음
		for (int j = commands[i][0] - 1; j < commands[i][1]; j++)
			temp.push_back(array1[j]);
		//임시 벡터정렬
		sort(temp.begin(), temp.end());
		//임시벡터의 index번째를 answer에 넣음
		answer.push_back(temp.at(commands[i][2] - 1));
	}
	return answer;
}

void print(vector<int> array1, vector<vector<int>> commands, vector<int> answer) {
	vector<int> t = solution(array1, commands);
	if (t == answer)
		cout << "정답" << endl;
	else
		cout << "틀림 "<< endl;
}

int main(){
	print({ 1, 5, 2, 6, 3, 7, 4 }, { {2, 5, 3},{4, 4, 1},{1, 7, 3} }, {5, 6, 3});
	return 0;
}