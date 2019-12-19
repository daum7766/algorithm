#include <iostream>
#include <string>

using namespace std;

int main() {
	string a;
	int sum{};
	cin >> a;
	//반복문을 이용해서 한글자씩 접근;
	//char는 -'0'을 하면 숫자가 된다.
	for (auto t : a) 	sum += t - '0';
	//sum을 3으로 나눈값이 0이라면 3의 배수이다.
	if (!(sum % 3))	cout << 1 << endl;
	else	cout << 0 << endl;
	return 0;
}