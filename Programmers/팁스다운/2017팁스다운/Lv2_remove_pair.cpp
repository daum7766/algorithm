#include <string>
#include <stack>
#include <iostream>
using namespace std;

int solution(string s) {
	stack<char> str;
	//처음부터 끝까지 순회
	for (int i = 0; i < s.length(); i++) {
		//스택이 비어있거나 탑하고 현재글자가 다르다면 스택에 푸쉬
		if (str.empty() || str.top() != s[i])	str.push(s[i]);
		//탑과 현재글자가 같다면 탑에있는 글자제거
		else if (str.top() == s[i])		str.pop();
	}
	//스택이 비어있다면 모두제거한것이므로 1리턴
	if (str.empty())	return 1;
	return 0;
}

void print(string s, int answer) {
	int t = solution(s);
	if (t == answer)
		cout << "정답" << endl;
	else
		cout << "틀림" << endl;
}

int main() {
	print("baabaa", 1);
	print("cdcd", 0);
	return 0;
}