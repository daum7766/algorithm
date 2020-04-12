#include <iostream>

using namespace std;

int main() {
	//11*10 배열
	int arr[11][10]{ 0 };
	//값 입력받기
	for (int i = 0; i < 11; i++) {
		for (int j = 0; j < 10; j++) {
			cin >> arr[i][j];
		}
	}
	//진군하면서체크하기
	for (int j = 0; j < 10; j++) {
		for (int i = 9; i >= 0; i--) {
			//값이 비어있다면 패스하기
			if (!arr[10][j]) 		break;
			//평지라면 진행, 마지막까지갔다면 safe출력
			if (!arr[i][j]) {
				if (!i)	cout << j + 1 << " safe" << endl;
				continue;
			}
			//장에물을 만났다면 crash출력하고 다음으로 넘어가기
			else if (arr[i][j] > 0) {
				cout << j + 1 << " crash" << endl;
				break;
			}
			//구덩이를 만났다면 fall을 출력하고 다음으로 넘어가기
			else if (arr[i][j] < 0) {
				cout << j + 1 << " fall" << endl;
				break;
			}
		}
	}
	return 0;
}