#include <iostream>
using namespace std;

int t_count[100001] = { 1, 1, 2, 4 };

int Recursion(int r)
{
	if (t_count[r] != 0)
	{
		return t_count[r];
	}
	else
	{
		return t_count[r] = (Recursion(r - 3) + Recursion(r - 2) + Recursion(r - 1)) % 1000;
	}
}


int main()
{
	int r;
	cin >> r;
	Recursion(r);
	cout << t_count[r] << endl;
	return 0;
}
