#include <string>
#include <vector>
#include <iostream>
#include <map>

using namespace std;


int solution(string skill, vector<string> skill_trees) {
	int answer = 0;
	map<char, int> tree;
	//해쉬맵에 스킬순서를 저장
	for (int i = 0; i < skill.length(); i++)
		tree[skill[i]] = i + 1;
	//스킬트리 순회하기
	for (auto skt : skill_trees) {
		int count = 1;
		bool check = true;
		//현재 스킬이 스킬트리에 위배되는지 확인
		for (int i = 0; i < skt.length(); i++) {
			//스킬순서가 맞지않다면 탈출
			if (tree[skt[i]] > count) {
				check = false;
				break;
			}
			//최소 스킬트리를 익혔다면 다음스킬을 익힐수있도록 증가
			else if (tree[skt[i]] == count)
				count++;
		}
		//이상잆어 통과했다면 모든 스킬을 배울수있으므로 카운트 증가
		if (check)
			answer++;
	}
	return answer;
}

void print(string skill, vector<string> skill_trees, int answer) {
	int t = solution(skill, skill_trees);
	//cout << t << " , ";
	if (answer == t)
		cout << "정답" << endl;
	else
		cout << "틀림" << endl;
}

int main() {
	print("CBD", { "BACDE", "CBADF", "AECB", "BDA" }, 2);
	return 0;
}
