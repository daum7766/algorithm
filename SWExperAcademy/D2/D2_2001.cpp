#include <iostream>
#include <string>
using namespace std;
int main() {
	//총 반복길이, 칸넓이, 파리채크기, 최대리스트
	int length, n, m, list[15][15];
	cin >> length;
	//총 반복만큼
	for (int i = 1; i <= length; i++) {
		int max = 0;
		cin >> n >> m;
		//파리개수를 입력받는다.
		for (int j = 0; j < n; j++) {
			for (int k = 0; k < n; k++) {
				cin >> list[j][k];
			}
		}
		//오른쪽과 아래로 이동하면서 파리수를 더하여 최대파리수 계산
		for (int j = 0; j <= n - m; j++) {
			for (int k = 0; k <= n - m; k++) {
				//여기까지가 파리채 이동
				int sum = 0;
				//여기부터가 파리수 더하기
				for (int x = j; x < j + m; x++) {
					for (int y = k; y < k + m; y++) {
						sum += list[x][y];
					}
				}
				//최대값과 비교하여 더크다면 바꾸기
				if (sum > max)        max = sum;
			}
		}
		cout << "#" << i << " " << max << endl;
	}
	return 0;
}