#include <iostream>
#include <string>

using namespace std;


string Decimal_To_Binary(int a, string sum)
{
	sum = to_string(a % 2) + sum;
	if (a <= 1)
	{
		return sum;
	}
	return Decimal_To_Binary(a / 2, sum);
}

int main()
{
	int n;
	cin >> n;
	cout << Decimal_To_Binary(n, "") << endl;
	return 0;
}
