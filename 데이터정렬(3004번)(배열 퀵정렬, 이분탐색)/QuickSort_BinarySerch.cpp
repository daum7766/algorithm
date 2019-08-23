#include <iostream>

using namespace std;
int t_array[50000];
int temp[50000];

//퀵정렬
void Quick_Sort(int* data, int start, int end)
{
	if (start >= end)
	{
		//원소가 1개 이하일 경우 재귀호출 중지
		return;
	}

	int pivot = start;
	int i = pivot + 1;
	int j = end;
	int temp;

	while (i <= j)
	{
		//i가 끝까지 가거나 기준점보다 작을때까지 i증가
		while (i <= end && data[i] <= data[pivot])
		{
			i++;
		}
		//j가 처음까지 가거나 기준점보다 클때까지 j 감소
		while (j > start && data[j] >= data[pivot])
		{
			j--;
		}

		if (i > j)
		{
			//포인터가 엇갈렸다면 퀵정렬끝 pivot 교환
			temp = data[j];
			data[j] = data[pivot];
			data[pivot] = temp;
		}
		else
		{
			//i번째와 j번째를 교체
			temp = data[i];
			data[i] = data[j];
			data[j] = temp;
		}
	}
	//재귀호출
	Quick_Sort(data, start, j - 1);
	Quick_Sort(data, j + 1, end);
}

int BinarySerch(int* data, int targetNum, int start, int end)
{
	int pivot = (start + end) / 2;
	if (targetNum == data[pivot])
	{
		return pivot;
	}
	else if (targetNum < data[pivot])
	{
		return BinarySerch(data, targetNum, start, pivot - 1);
	}
	else if (targetNum > data[pivot])
	{
		return BinarySerch(data, targetNum, pivot + 1, end);
	}
}

int main()
{
	int length;
	cin >> length;
	int t;
	for (int i = 0; i < length; i++)
	{
		cin >> t;
		t_array[i] = t;
		temp[i] = t;
	}
	Quick_Sort(t_array, 0, length - 1);

	for (int i = 0; i < length; i++)
	{
		cout << BinarySerch(t_array, temp[i], 0, length) << " ";
	}

	return 0;
}