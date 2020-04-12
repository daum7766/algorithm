#include <string>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

string solution(int n) {
	string answer = "";
	string temp[3]{ "4", "1", "2" };
	//n이 0이 될때까지 반복
	while (n) {
		//1,2,4 4개의 숫자를 사용하므로 3 나머지 연산
		//0일경우 4로 대체
		answer = temp[n % 3] + answer;
		//나머지가 0일경우 -1을 해줘야 몫이 사라짐, 아니면 3일경우 14가 나옴
		if (!(n % 3))
			n = n / 3 - 1;
		else
			n = n / 3;
	}
	return answer;
}


void print(int N, string answer) {
	string t = solution(N);
	cout << t << " , ";
	if (answer == t)
		cout << "정답" << endl;
	else
		cout << "틀림" << endl;
}

int main() {

	print(1, "1");
	print(2, "2");
	print(3, "4");
	print(4, "11");
	print(5, "12");
	print(6, "14");
	print(7, "21");
	print(8, "22");
	print(9, "24");
	print(10, "41");
	return 0;
}