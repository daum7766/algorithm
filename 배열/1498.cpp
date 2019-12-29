#include <iostream>
#include <algorithm>

using namespace std;

int main() {
	//들어오는 개수, 묶는 단위, 배열
	int length, g, a[100]{ 1000 };
	cin >> length >> g;
	//입력받기
	for (int i = 0; i < length; i++) 	cin >> a[i];
	//g만큼씩 증가시키며 반복
	for (int i = 0; i < length; i += g) {
		int num = a[i];
		//묶음만큼 반복처리
		for (int j = 0; j < g; j++) {
			//들어오는 데이터의 크기를넘어갔다면 정지
			if (i + j >= length)	break;
			//작은것 찾기
			num = min(num, a[i + j]);
		}
		cout << num << " ";
	}
	return 0;
}