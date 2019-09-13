#include <iostream>

using namespace std;

struct MyStruct
{
	int num;
	int gas;
};

//퀵정렬
void Quick_Sort(MyStruct* data, int start, int end)
{
	if (start >= end)
	{
		//원소가 1개 이하일 경우 재귀호출 중지
		return;
	}

	int pivot = start;
	int i = pivot + 1;
	int j = end;
	MyStruct temp;

	while (i <= j)
	{
		//i가 끝까지 가거나 기준점보다 작을때까지 i증가
		while (i <= end && data[i].num <= data[pivot].num)
		{
			i++;
		}
		//j가 처음까지 가거나 기준점보다 클때까지 j 감소
		while (j > start && data[j].num >= data[pivot].num)
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

MyStruct myStructs[100];

int main()
{
	int a, b, length = 0;
	cin >> length;
	for (int i = 0; i < length; i++)
	{
		cin >> a >> b;
		myStructs[i].num = a;
		myStructs[i].gas = b;
	}
	Quick_Sort(myStructs, 0, length - 1);
	for (int i = 0; i < length; i++)
	{
		cout << myStructs[i].num << " " << myStructs[i].gas << endl;
	}


	return 0;
}