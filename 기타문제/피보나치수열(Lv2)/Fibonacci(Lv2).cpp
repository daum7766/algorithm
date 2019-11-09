#include <string>
#include <vector>
#include <iostream>

using namespace std;

int memo[100000]{ 0 };

int Fibonacci(int n) {
	if (memo[n - 1])
		return memo[n - 1];
	return memo[n - 1] = (Fibonacci(n - 2) + Fibonacci(n - 1)) % 1234567;
}

int solution(int n) {
	memo[0] = 1;
	memo[1] = 1;
	int answer = Fibonacci(n);
	return answer;
}

void print(int nums, int answer) {
	int t = solution(nums);
	cout << t << " , ";
	if (answer == t)
		cout << "정답" << endl;
	else
		cout << "틀림" << endl;
}
///*
int main() {
	print(3, 2);
	print(5, 5);

	return 0;
}
//*/