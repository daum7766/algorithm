#include <iostream>

using namespace std;

int main() {
	//배열크기, 시작점x, 시작점y, 2차원배열, 계산용1, 계산용2
	int n, x, y, arr[100][100], x1, y1;
	cin >> n >> x >> y;
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			//x,y좌표에서 떨어진만큼 더해서 계산한다.
			//좌표가 0이아니라 1부터시작하므로 1개씩 빼준다.
			//값이 0이 아니라 1부터 시작하므로 결과값에 1을 더해준다.
			x1 = abs(x - 1 - i);
			y1 = abs(y - 1 - j);
			arr[i][j] = x1 + y1 + 1;
			cout << arr[i][j] << " ";
		}
		cout << endl;
	}
	return 0;
}