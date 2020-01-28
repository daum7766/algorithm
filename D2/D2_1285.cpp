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
			distance = abs(distance);
			if (distance < min) {
				min = distance;
				count = 1;
			}
			else if (distance == min)
				count++;
		}
		cout << "#" << l << " " << min << " " << count << endl;
	}
	return 0;
}