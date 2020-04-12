#include <string>
#include <vector>
#include <sstream>
#include <algorithm>

using namespace std;

string solution(string s) {
	vector<int> list;
	string answer = "";
	stringstream sst;
	sst.str(s);
	while (sst >> answer)
		list.push_back(stoi(answer));
	int max = *max_element(list.begin(), list.end());
	int min = *min_element(list.begin(), list.end());
	return to_string(min) + " " + to_string(max);
}

void print(string s, string answer) {
	string t = solution(s);
	if (t == answer)
		cout << "정답" << endl;
	else
		cout << "틀림" << endl;
}

int main() {
	print("1 2 3 4", "1 4");
	print("-1 -2 -3 -4", "-4 -1");
	print("-1 -1", "-1 -1");
	return 0;
}