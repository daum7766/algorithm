#include <iostream>
#include <vector>
#include <string>
using namespace std;
//D2 1961 숫자 배열 회전

//배열회전함수
void spin_arr(int N, vector<vector<string>> &arr) {
	vector<vector<string>> temp(N, vector<string>(N, ""));
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++)
			temp[i][j] = arr[abs(j - (N - 1))][i];
	}
	arr = temp;
}

int main() {
	int len;
	cin >> len;
	//입력받은 횟수만큼 반복
	for (int l = 1; l <= len; l++) {
		int N, row = 0, cul = 0;
		cin >> N;
		//입력받은 배열과 결과배열
		vector<vector<string>> arr(N, vector<string>(N, "")), result(N, vector<string>(N, ""));
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < N; j++)
				cin >> arr[i][j];
		}
		//배열은 총 3번 회전시킨다.
		for (int l = 0; l < 3; l++) {
			spin_arr(N, arr);
			row = 0;
			//회전시킨후 결과저장
			for (int i = 0; i < N; i++) {
				for (int j = 0; j < N; j++) 
					result[row][cul] += arr[i][j];
				row++;
			}
			cul++;
		}
		//출력
		cout << "#" << l << endl;
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < N; j++)
				cout << result[i][j] << " ";
			cout << endl;
		}
	}
	return 0;
}