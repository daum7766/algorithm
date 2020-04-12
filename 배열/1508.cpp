#include <iostream>

using namespace std;

int main() {
	int arr[20][21]{ 0 }, len;
	//세로길이 입력
	cin >> len;
	//데이터 받기
	for (int i = 0; i < len; i++) 	cin >> arr[i][0];
	//데이터 계산
	//왼쪽데이터에서 왼쪽위에 데이터를 빼준다
	for (int i = 1; i < len; i++) {
		for (int j = 1; j <= i; j++) {
			arr[i][j] = arr[i][j - 1] - arr[i - 1][j - 1];
		}
	}
	//데이터 출력
	for (int i = 0; i < len; i++) {
		for (int j = 0; j <= i; j++)
			cout << arr[i][j] << " ";
		cout << endl;
	}
	return 0;
}