#include <iostream>
#include <algorithm>
using namespace std;
//1285 D2 아림이의 돌던지기
int main() {
	int len;
	cin >> len;
	for (int l = 1; l <= len; l++){
		int count = 0, min = 100000, n, distance;
		cin >> n;
		for (int i = 0; i < n; i++) {
			cin >> distance;
			// 거리를 절대값으로 바꾼다.
			distance = abs(distance);
			//거리가 최소거리보다 작다면 바꿔주기
			if (distance < min) {
				min = distance;
				count = 1;
			}
			//현재 최소거리와 같은사람이 있다면 카운트 증가
			else if (distance == min)
				count++;
		}
		cout << "#" << l << " " << min << " " << count << endl;
	}
	return 0;
}