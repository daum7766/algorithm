#include <iostream>

using namespace std;

int main() {
	bool arr[101][101]{ false };
	int x1, x2, y1, y2, answer = 0;
	for (int i = 0; i < 4; i++) {
		cin >> x1 >> y1 >> x2 >> y2;
		//차지하는 영역체크
		for (int j = x1; j < x2; j++) {
			for (int k = y1; k < y2; k++) {
				if (arr[j][k])	continue;
				answer++;
				arr[j][k] = true;
			}
		}
	}
	cout << answer << endl;
	return 0;
}