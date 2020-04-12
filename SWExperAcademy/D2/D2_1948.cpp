#include <iostream>

using namespace std;
//1948 D2 날짜 계산기
int main() {
	//전체 반복횟수
	int len, days[12]{31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
    //달과 일을 입력받음
	int month[2], day[2];
	cin >> len;
	for (int l = 1; l <= len; l++) {
		cin >> month[0] >> day[0] >> month[1] >> day[1];
		int result = 0;
        //달의 차이만큼 날짜 더해주기
		for (int i = month[0] - 1; i < month[1] - 1; i++) {
			result += days[i];
		}
		result += day[1] - (day[0] - 1);
		cout << "#" << l << " " << result << endl;
	}
	return 0;
}