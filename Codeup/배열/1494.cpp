#include <iostream>

using namespace std;

int main() {
	int k, n, arr[101]{ 0 }, arr2[101]{ 0 }, arr3[3];
	cin >> k >> n;
	//n개만큼의 데이터가 들어온다
	for (int i = 1; i <= n; i++) {
		//데이터는 s, e, u 순으로 들어온다.
		cin >> arr3[0] >> arr3[1] >> arr3[2];
		//d[s] = d[s] + u;
		arr[arr3[0]] = arr[arr3[0]] + arr3[2];
		//d[e+1] = d[e+1] - u;
		arr[arr3[1] + 1] = arr[arr3[1] + 1] - arr3[2];
	}
	//1차원 배열상태 출력하기
	for (int i = 1; i <= k; i++)		cout << arr[i] << " ";
	cout << endl;
	for (int i = 1; i <= k; i++) {
		//이전 누적합 + 현재배열상태를 더하고 출력
		arr2[i] = arr2[i - 1] + arr[i];
		cout << arr2[i] << " ";
	}
	return 0;
}