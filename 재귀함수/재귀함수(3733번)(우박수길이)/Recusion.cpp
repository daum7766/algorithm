#include <iostream>
#include <map>
#define MAX 10000000

using namespace std;

unsigned short list[MAX + 1] = { 1,1,2 };
int count;

int Recursion(long long n)
{
	if (n <= MAX && list[n])//이미계산했다면 넘기기
	{
		return list[n];
	}
	if (n % 2 == 1)//홀수
	{
		//배열길이를 넘어서면 값만 보냄
		if (n > MAX)
		{
			return Recursion((3 * n) + 1) + 1;
		}
		else//메모이제이션
		{
			return list[n] = Recursion((3 * n) + 1) + 1;
		}

	}
	else//짝수
	{
		//배열길이를 넘어서면 값만 보냄
		if (n > MAX)
		{
			return Recursion(n / 2) + 1;
		}
		else//메모이제이션
		{
			return list[n] = Recursion(n / 2) + 1;
		}

	}
}

int main()
{
	int a, b;
	int index = 0, max = 0;
	cin >> a >> b;
	for (int i = b; i >= a; i--)
	{
		if (Recursion(i) > max)
		{
			index = i;
			max = Recursion(i);
		}
		else if (Recursion(i) == max)
		{
			index = i;
		}
	}
	cout << index << " " << max << endl;

	return 0;

}