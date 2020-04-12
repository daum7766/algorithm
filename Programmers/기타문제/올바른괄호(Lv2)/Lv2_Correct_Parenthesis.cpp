#include <string>
#include <vector>
#include <iostream>

using namespace std;

bool solution(string s) {
	int count = 0;
	//문자열 순회
	for (auto st : s) {
		//괄호가 열린괄호이면 카운트증가
		if (st == '(')
			count++;
		//닫힌괄호인데 열린괄호가 1개이상 있다면 카운트 감소
		else if (st == ')' && count > 0)
			count--;
		//이외에는 false 리턴
		else
			return false;
	}
	//0일때만 트루 리턴
	return !count;
}

void print(string s, bool answer) {
	bool t = solution(s);
	//cout << t << " , ";
	if (answer == t)
		cout << "정답" << endl;
	else
		cout << "틀림" << endl;
}

int main() {
	print("()()", true);
	print("(())()", true);
	print(")()(", false);
	print("(()(", false);
	return 0;
}
