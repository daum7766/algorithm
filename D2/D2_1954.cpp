#include <iostream>
#include <vector>
using namespace std;

int main() {
	int n, row, cal, limit, r, len;
	cin >> len;
	for (int l = 1; l <= len; l++) {
		cin >> n;
		int row = 0, cal = -1, limit = 0, r = 1;
		vector<vector<int>> a(n, vector<int>(n, 0));
		for (int i = 1; i <= n * n;) {
			for (int j = 0; j < n - limit; j++) {
				cal += r;
				a[row][cal] = i++;
			}
			for (int j = 1; j < n - limit; j++) {
				row += r;
				a[row][cal] = i++;
			}
			limit++;
			r *= -1;
		}
		cout << "#" << l << endl;
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < n; j++) {
				cout << a[i][j] << ' ';
			}
			cout << endl;
		}
	}
	return 0;
}