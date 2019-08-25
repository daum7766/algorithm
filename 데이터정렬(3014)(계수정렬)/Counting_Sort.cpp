#include <iostream>
#include <stdio.h>

using namespace std;

int a_array[4500000];
int b_array[100001] = { 0 };

void Counting_Sort(int* data, int start, int end)
{
	for (int i = 0; i < end; i++)
	{
		b_array[data[i]]++;
	}
}

int main()
{
	int length;
	cin >> length;

	for (int i = 0; i < length; i++)
	{
		//cin >> a_array[i];
		scanf("%d", &a_array[i]);
	}
	Counting_Sort(a_array, 0, length);

	for (int i = 0; i <= 100000; i++)
	{
		for (int j = 0; j < b_array[i]; j++)
		{
			//cout << i << " ";
			printf("%d ", i);
		}
	}

	return 0;
}
