#include <string>
#include <vector>
#include <iostream>

using namespace std;
/*
유클리드 알고리즘
*/

//최대 공약수
int gcd(int a, int b) {
	int c;
	while (b != 0) {
		c = a % b;
		a = b;
		b = c;
	}
	return a;
}
//최소 공배수
int lcm(int a, int b, int c) {
	return a * b / c;
}

vector<int> solution(int n, int m) {
	vector<int> answer;
	answer.push_back(gcd(n, m));
	answer.push_back(lcm(n, m, answer.at(0)));
	return answer;
}

void print(int n, int m, vector<int> answer) {
	vector<int> t = solution(n, m);
	if (answer == t)
		cout << "정답" << endl;
	else
		cout << "틀림" << endl;
}

int main() {
	print(3, 12, { 3, 12 });
	print(2, 5, { 1, 10 });
	return 0;
}
