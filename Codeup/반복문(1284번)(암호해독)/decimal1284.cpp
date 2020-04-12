#include <iostream>
#include <cmath>
using namespace std;

bool Decheck(int a)
{
	int i = 2;
	while (1) { //무한루프 
		if (i <= sqrt(a)) {
			if (a % i == 0) { //i가 나누어떨어지면 소수가 아님 
				return false;
			}
			else {
				i++;
			}
		}
		else { //i가 j보다 커질때까지 나누어떨어지지 않으면 소수 
			return true;
		}
	}
}

int main()
{
	int num;
	cin >> num;
	for (int i = 2; i < num; i++)
	{
		if (Decheck(i))
		{
			if (num % i == 0 && Decheck(num / i))
			{
				cout << i << " " << num / i << endl;
				return 0;
			}
		}
	}
	cout << "wrong number" << endl;
	return 0;
}
