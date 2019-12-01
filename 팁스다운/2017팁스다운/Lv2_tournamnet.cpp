#include <iostream>
using namespace std;

int solution(int n, int a, int b) {
	int answer = 0;
	while (a != b) {
		a = (a + 1) >> 1;
		b = (b + 1) >> 1;
		answer++;
	}
	return answer;
}

void print(int n, int a, int b, int answer) {
	int t = solution(n, a, b);
	if (t == answer)	cout << "정답" << endl;
	else	cout << "실패" << endl;
}

int main() {
	print(8, 4, 7, 3);
	return 0;
}
