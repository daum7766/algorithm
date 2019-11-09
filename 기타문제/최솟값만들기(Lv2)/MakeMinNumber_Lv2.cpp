#include <string>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

int solution(vector<int> A, vector<int> B) {
	int answer = 0, Index = -1, size = B.size();
	sort(A.begin(), A.end());
	sort(B.begin(), B.end());
	while (++Index != size) {
		answer += A[Index] * B[size - 1 - Index];
	}
	return answer;
}

void print(vector<int> A, vector<int> B, int answer) {
	int t = solution(A, B);
	cout << t << " , ";
	if (answer == t)
		cout << "정답" << endl;
	else
		cout << "틀림" << endl;
}
///*
int main() {

	print({ 1,4,2 }, { 5,4,4 }, 29);
	print({ 1,2 }, { 3, 4 }, 10);
	return 0;
}
//*/