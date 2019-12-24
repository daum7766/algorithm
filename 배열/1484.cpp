#include <iostream>

using namespace std;

int main() {
	int a[100][100]{ 0 }, n, m, row = 0, col = -1, reverse = 1;
	cin >> n >> m;
	int limit = 0;
	//총반복의 횟수는 n*m의 숫자까지
	for (int count = 1; count <= n * m;) {
		//가로채우기
		for (int i = 0; i < m - limit; i++) {
			col += reverse;
			a[row][col] = count++;
		}
		//세로 채우기
		for (int i = 0; i < n - limit - 1; i++) {
			row += reverse;
			a[row][col] = count++;
		}
		//최대 반복횟수 감소
		limit++;
		//반복이 한번될때마다 역전시킨다.
		reverse = -reverse;
	}

	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++)
			cout << a[i][j] << " ";
		cout << endl;
	}
	return 0;
}