#include <iostream>

using namespace std;

int main() {
	int a[100][100], n, m;
	cin >> n >> m;
	for (int j = 0, count = 1; j <= n + m - 2; j++) {
		for (int i = 0; i < n; i++) {
			//제일 오른쪽 열부터 시작한다.
			for (int k = m - 1; k >= 0; k--) {
				//규칙을 찾으면 m- 1 -k +i를 하면 규칙적인 합이나온다.
				if (i + (m - 1 - k) == j) {
					a[i][k] = count++;
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