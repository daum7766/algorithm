#include <iostream>

using namespace std;

int main() {
	int n, m, temp, arr[100][100]{ 0 }, arr2[100][100]{ 0 };
	cin >> n >> m;
	//기본배열에 값을 입력받는다.
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			cin >> arr[i][j];
		}
	}
	//두번째 배열에 이전까지 있던 합들을 더한다.
	//ex) 1,1 이라면 (0, 0), (0, 1), (1, 0), (1, 1)을 더해준다.
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			for (int k = 0; k <= i; k++) {
				for (int z = 0; z <= j; z++) {
					arr2[i][j] += arr[k][z];
				}
			}
		}
	}
	//더한 값들을 출력
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			cout << arr2[i][j] << " ";
		}
		cout << endl;
	}
	return 0;
}