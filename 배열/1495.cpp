#include <iostream>

using namespace std;

int main() {
	int k, n, d[1001][1001]{ 0 }, arr[1001][1001]{ 0 }, x1, x2, y1, y2, u, m;
	cin >> k >> m >> n;
	//n개만큼의 데이터가 들어온다
	//공식대로 처리한다.
	for (int i = 0; i < n; i++) {
		cin >> x1 >> y1 >> x2 >> y2 >> u;
		d[x1][y1] += u;
		d[x2 + 1][y2 + 1] += u;
		d[x1][y2 + 1] -= u;
		d[x2 + 1][y1] -= u;
	}
	//기본 배열상태 출력
	for (int i = 0; i < k; i++) {
		for (int j = 0; j < m; j++) {
			cout << d[i][j] << " ";
		}
		cout << endl;
	}
	cout << endl;
	//시간을 단축하기 위해 조건문 사용
	//자신의 왼쪽과 위를 더한거에 i-1 j-1을 빼면 중복된 부분이 제거가 된다.
	for (int i = 0; i < k; i++) {
		for (int j = 0; j < m; j++) {
			if (!i && !j)	arr[i][j] = d[i][j];
			else if (!i)	arr[i][j] = arr[i][j - 1] + d[i][j];
			else if (!j)	arr[i][j] = arr[i - 1][j] + d[i][j];
			else	arr[i][j] = arr[i][j - 1] + arr[i - 1][j] - arr[i - 1][j - 1] + d[i][j];
			cout << arr[i][j] << " ";
		}
		cout << endl;
	}
	return 0;
}