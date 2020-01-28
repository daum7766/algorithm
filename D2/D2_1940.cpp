#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
//1940 D2 가랏! RC카!
int main() {
	//전체 반복횟수 입력받고 반복
	int len, len2;
	cin >> len;
	for (int l = 1; l <= len; l++) {
		//명령횟수만큼 반복
		cin >> len2;
		//현재 스피트, 이동한거리, 가속도, 명령넘버(0유지, 1가속, 2감속)
		int now_speed = 0, distance = 0, speed = 0, num = 0;
		for (int l2 = 0; l2 < len2; l2++) {
			cin >> num;
			//0일경우 무시
			if (!num) {	}
			//1일경우 가속
			else if (num & 1) {
				cin >> speed;
				now_speed += speed;
			}
			//2일경우 감속
			else {
				cin >> speed;
				now_speed -= speed;
				//속도가 0보다 작아지면 0으로 변경
				if (now_speed < 0)
					now_speed = 0;
			}
			//거리에 이동속도 더하기
			distance += now_speed;
		}
		cout << "#" << l << " " << distance << endl;
	}
	return 0;
}