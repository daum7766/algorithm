#include <vector>
#include <iostream>
using namespace std;

//최대공약수 구하기
int gcd(int a, int b) { return !(a % b) ? b : gcd(b, a % b); }
//최소 공배수 구하기
int lcm(int a, int b) { return a * b / gcd(a, b); }

int solution(vector<int> arr) {
	int answer = arr[0];
	// 2개의 최소공배수를 구해서 다음꺼와 다시 최소공배수를 구한다.(복잡도 O(N))
	for (int i = 1; i < arr.size(); i++)	answer = lcm(answer, arr[i]);
	return answer;
}

void print(vector<int> arr, int answer) {
	int t = solution(arr);
	if (t == answer)	cout << "정답" << endl;
	else	cout << "실패" << endl;
}

int main() {
	print({ 2, 6, 8, 14 }, 168);
	print({ 1, 2, 3 }, 6);
	return 0;
}