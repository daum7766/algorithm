#include <iostream>
#include <string>

using namespace std;

int main() {
	int a[100][100]{ 0 }, n, sum = 0;
	cin >> n;
	//배열에 값채우기
	for (int i = 0, count = 1; i < n; i++) {
		for (int j = 0; j < n; j++) {
			a[i][j] = count++;
		}
	}
	//위아래 줄 더하기
	for (int i = 0; i < n; i++) {
		sum += a[0][i];
		sum += a[n - 1][i];
	}
	//양 옆 테두리 더하기(겹치는 부분 제외)
	for (int i = 1; i < n - 1; i++) {
		sum += a[i][0];
		sum += a[i][n - 1];
	}
	cout << sum << endl;

	return 0;
}

