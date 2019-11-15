#include <string>
#include <vector>
#include <algorithm>
#include <iostream>
#include <map>

using namespace std;
vector<string> combination;
int column = 0;

//string 비교함수 길이로 먼저 정렬을하고 같으면 큰순서대로 정렬한다
bool compare(string& a, string& b) {
	if (a.length() != b.length()) 	return a.length() < b.length();
	return a < b;
}

//모든 조합을 만드는 함수
void Combination(int k = 0, string temp = "") {
	for (int i = k; i < column; i++) {
		temp += to_string(i);
		combination.push_back(temp);
		Combination(i + 1, temp);
		temp = temp.substr(0, temp.length() - 1);
	}
}

//조합에따른 후보키 판단 함수
bool subset(vector<vector<string>>& relation, string com) {
	map<string, int> candidateCheck;
	for (int i = 0; i < relation.size(); i++) {
		//후보키 조합에 따른 string 함침
		string temp = "";
		for (int k = 0; k < com.length(); k++) {
			int number = com[k] - '0';
			temp += relation[i][number] + " ";
		}
		//뒤에 들어간 띄어쓰기 삭제(안해도 무방함)
		temp = temp.substr(0, temp.length() - 1);
		//만약 이미 있었다면 후보키가 될수없다고 반환
		if (candidateCheck[temp])	return false;
		//map에 합친 string값을 추가
		candidateCheck[temp]++;
	}
	//끝까지 중복이 없었다면 최소성과 유일성을 만족시켰다. true 리턴
	return true;
}

int solution(vector<vector<string>> relation) {
	int answer = 0;
	//칼럼 개수 추가
	column = relation[0].size();
	//가능한 조합수 가져오기
	Combination();
	//가능한 조합수 정렬하기(낮은 조합부터 하기위해)-> 이걸 안해서 한동안 고생함
	sort(combination.begin(), combination.end(), compare);
	//조합수만큼 반복
	for (int i = 0; i < combination.size(); i++) {
		//후보키라면
		if (subset(relation, combination[i])) {
			//후보키를 임시변수에 넣는다.
			string temp = combination[i];
			//후보키에 와 겹치는 조합은 다 없앤다. 13조합이면 1과 3이들어간것을 모두찾아서 제거
			for (int j = combination.size() - 1; j >= i; j--) {
				bool check = true;
				for (auto t : temp) {
					if (combination[j].find(t) == string::npos) {
						check = false;
						break;
					}
				}
				//하나도 없었으면 패스를 위한 조건문
				if (check)	combination.erase(combination.begin() + j);
			}
			//제거를 했으므로 i를 감소하고 후보키였으므로 answer증가
			i--;	answer++;
		}
	}
	return answer;
}

void print(vector<vector<string>> relation, int answer) {
	int t = solution(relation);
	if (answer == t)
		cout << "정답" << endl;
	else
		cout << "틀림" << endl;
}

int main() {

	print({ {"100", "ryan", "music", "2"}, {"200", "apeach", "math", "2"},
		{"300", "tube", "computer", "3"}, {"400", "con", "computer", "4"},
		{"500", "muzi", "music", "3"}, {"600", "apeach", "music", "2"} }, 2);
	return 0;
}
