#include <iostream>
#include <string>

using namespace std;

int main() {
	string a;
	int sum{};
	cin >> a;
	for (auto t : a) 	sum += t - '0';
	if (!(sum % 3))	cout << 1 << endl;
	else	cout << 0 << endl;
	return 0;
}
