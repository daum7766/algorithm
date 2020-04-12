#include <string>
#include <vector>
#include <iostream>
#include <map>
#include <queue>
#include <sstream>

using namespace std;



vector<string> solution(vector<string> record) {
	vector<string> answer;
	//아이디와 닉네임 매치
	map<string, string> names;
	string order[3] = { "Enter", "Leave", "Change" };
	string t_order{}, uid{}, name{};
	//문자열 분할용
	stringstream ss;

	for (auto r : record) {
		ss.str(r);
		ss >> t_order;
		//명령어가 Enter 혹은 Change라면 map에 아이디와 이름변경
		if (t_order == order[0] || t_order == order[2]) {
			ss >> uid;
			ss >> name;
			names[uid] = name;
		}
		ss.clear();
	}
	//Enter 혹은 Leave라면 map에서 이름을 가져와 출력
	for (auto r : record) {
		ss.str(r);
		ss >> t_order;
		ss >> uid;
		if (t_order == order[0])
			answer.push_back(names[uid] + "님이 들어왔습니다.");
		else if (t_order == order[1])
			answer.push_back(names[uid] + "님이 나갔습니다.");
		ss.clear();
	}

	return answer;
}

void print(vector<string> record, vector<string> answer) {
	vector<string> t = solution(record);
	if (answer == t)
		cout << "정답" << endl;
	else
		cout << "틀림" << endl;
}

int main() {
	print({ "Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan" },
		{ "Prodo님이 들어왔습니다.", "Ryan님이 들어왔습니다.", "Prodo님이 나갔습니다.", "Prodo님이 들어왔습니다." });
	return 0;
}