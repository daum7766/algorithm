#include <iostream>
#include <string>
using namespace std;
//D3 8821 적고 지우기

int main() {
	int len;
	cin >> len;
	//입력받은 횟수만큼 반복
	for (int l = 1; l <= len; l++) {
		//각 자리수 상태를 체크하기 위해 표시
		//false라면 없는것이고 true라면 있는것이다.
		bool arr[10]{false};
		int count = 0;
		string num;
		cin >> num;
		//문자열을 입력받고 돌린다.
		for (int i = 0; i < num.size(); i++) {
			//char형에서 숫자로 변환하고 싶다면 - '0'을 처리하면 된다.
			int temp = num[i] - '0';
			//배열안에 있는 값을 뒤집는다.
			arr[temp] = !arr[temp];
		}
		//true인 것들을 찾아 카운팅한다.
		for (int i = 0; i < 10; i++)
			if (arr[i])	count++;
		cout << "#" << l << " " << count << endl;

	}
	return 0;
}