#include  <iostream>

using namespace std;

int Greatest_Common_divisor(int a, int b)
{
	int temp;
	while (a % b != 0)
	{
		temp = b;
		b = a % b;
		a = temp;
	}
	return b;

}

int main()
{
	int a, b;
	cin >> a >> b;
	cout << Greatest_Common_divisor(a, b) << endl;
	return 0;
}