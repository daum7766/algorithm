#include <iostream>

using namespace std;

int t_array[1000];

int Bubble_Sort(int* data, int length)
{
	bool check = true;
	int result = 0;
	for (int i = 0; i < length; i++)
	{
		for (int j = 0; j < length - i - 1; j++)
		{
			if (data[j] > data[j + 1])
			{
				int temp = data[j];
				data[j] = data[j + 1];
				data[j + 1] = temp;
				check = false;
				result = i + 1;
			}
		}
		if (check)
		{
			return result;
		}
		check = true;
	}
}

int main()
{
	int length;
	cin >> length;

	for (int i = 0; i < length; i++)
	{
		cin >> t_array[i];
	}
	cout << Bubble_Sort(t_array, length) << endl;

	return 0;
}