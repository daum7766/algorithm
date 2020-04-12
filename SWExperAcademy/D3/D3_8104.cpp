#include <iostream>
#include <vector>
using namespace std;

//D3 8104 조 만들기

int main(){
	int T, n, k = 0;
	cin >> T;
	for (int t = 1; t <= T; t++) {
		cin >> n >> k;
		vector<vector<int>> arr(k);
		int count = 1;
        //정방향, 역방향으로 계산
		for (int i = 0; count <= n*k; i++) {
			for (int j = 0; j < k; j++)
				arr[j].push_back(count++);
            //조원이 홀수인경우를 위해 멈춤
			if (count > n*k) break;
			for (int j = k-1; j>=0; j--)
				arr[j].push_back(count++);
		}
		cout << "#" << t << " ";
		for (int i = 0; i < k; i++) {
			int answer = 0;
			for (int j = 0; j < arr[i].size(); j++) {
				answer += arr[i][j];
			}
			cout << answer << ' ';
		}
		cout << endl;
	}
	return 0;
}