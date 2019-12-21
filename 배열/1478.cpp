#include <iostream>

using namespace std;

int main() {
	int a[100][100], n, m;
	cin >> n >> m;
	for (int j = 0, count = 1; j <= n + m - 2; j++) {
		for (int i = 0; i < n; i++) {
			for (int k = m - 1; k >= 0; k--) {
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