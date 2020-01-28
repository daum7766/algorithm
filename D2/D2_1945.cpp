#include <iostream>
#include <vector>

using namespace std;
//1945 D2 간단한 소인수 분해
int main() {
	//전체 반복횟수 입력받고 반복, 입력숫자, 나눌값
	int len, num, a[5] = { 11, 7, 5, 3, 2 };
	cin >> len;
	for (int l = 1; l <= len; l++) {
		//a~e까지 체크용
		vector<int> arr(5, 0);
		cin >> num;
		for (int i = 0; i < 5; i++) {
			//값이 0이 될때까지 반복
			while (num) {
				//나눌때 소숫자리가 발생하지 않는다면
				if ((num / a[i]) == (num / float(a[i]))) {
					//카운트 증가 후 나눈값 저장
					arr[i]++;
					num /= a[i];
				}
				//소숫자리가 나올경우 작은수로 넘어간다.
				else	break;
			}
		}
		cout << "#" << l;
		for (int i = 4; i >= 0; i--) {
			cout << " " << arr[i];
		}
		cout << endl;
	}
	return 0;
}