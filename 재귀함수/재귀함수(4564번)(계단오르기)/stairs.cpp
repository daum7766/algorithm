#include <iostream>
using namespace std;

int t_array[301];
int t_max[301];
int length;
int max = 0;
int Max_Check(int a, int b)
{
	return a >= b ? a : b;
}

int Recursion(int k)
{
	if (k < 1)
	{
		return 0;
	}
	if (t_max[k] != 0)
	{
		return t_max[k];
	}
	if (k == 1)
	{
		return t_max[k] = t_array[k];
	}
	if (k == 2)
	{
		return t_max[k] = t_array[k] + t_array[k - 1];
	}

	return t_max[k] = Max_Check(Recursion(k - 3) + t_array[k - 1], Recursion(k - 2)) + t_array[k];
}


int main()
{

	cin >> length;
	for (int i = 1; i <= length; i++)
	{
		cin >> t_array[i];
	}
	cout << Recursion(length) << endl;

	return 0;
}