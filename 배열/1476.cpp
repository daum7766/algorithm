#include <iostream>

using namespace std;

int main() {
	int a[100][100], n, m;
	bool check{ true };
	cin >> n >> m;
	//자리수를 더하면 같은수가 나온다.
	for (int j = 0, count = 1; j <= n + m - 2; j++) {
		//열 반복
		for (int i = 0; i < m; i++) {
			//행 반복
			for (int k = 0; k < n; k++) {
				//행과 열의 합이 j와 같다면 count 넣고 증가시키기
				if (i + k == j) {
					a[k][i] = count++;
					break;
				}
			}
		}
	}
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++)
			cout << a[i][j] << " ";
		cout << endl;
	}
	return 0;
}