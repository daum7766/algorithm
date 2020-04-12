#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
//1288 D2 새로운 불면증 치료법
int main() {
	//전체 반복횟수 입력받고 반복
	int len;
	cin >> len;
	for (int l = 1; l <= len; l++) {
		//n과 반복횟수를 나타내는 i, 숫자체크용 a
		int n, i = 1;
		vector<int> a(10, 1);
		cin >> n;
		bool check = false;
		//0~9까지 모든수가 나올때까지 반복
		for (i = 1; ; i++) {
			int temp = i * n;
			//한번도 걸리지 않았다면 반복문 탈출
			if (check)	break;
			check = true;
			//수를 쪼개면서 체크하기
			while (temp) {
				if (a[temp % 10])	a[temp % 10] = 0;
				temp /= 10;
			}
			//0번부터 9번까지 돌면서 모든값이 있나 체크하기
			for (int j = 0; j < 10; j++) {
				if (a[j]) {
					check = false;
					continue;
				}
			}
		}
		//값 출력하기
		cout << "#" << l << " " << (i-1)*n << endl;
	}
	return 0;
}