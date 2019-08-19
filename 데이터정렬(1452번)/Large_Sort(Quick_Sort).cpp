#include  <iostream>
#include <list>

using namespace std;

//퀵정렬 함수
list<int> Quick_sort(list<int> b, int t_lenth)
{
	//재귀함수 탈출조건
	if (t_lenth <= 1)
	{
		return b;
	}
	//기준점을 꺼내고 크기감소
	int pivot = *b.begin();
	b.pop_front();
	t_lenth--;
	//임시 리스트 설정
	list<int> t_a;
	int t_a_Lenth = 0;
	list<int> t_b;
	int t_b_Lenth = 0;
	//기준점과 비교하여 분리
	for (int i = 0; i < t_lenth; i++)
	{
		if (pivot >= *b.begin())
		{
			t_a.push_back(*b.begin());
			b.pop_front();
			t_a_Lenth++;
		}
		else
		{
			t_b.push_back(*b.begin());
			b.pop_front();
			t_b_Lenth++;
		}
	}
	//재귀함수 호출
	t_a = Quick_sort(t_a, t_a_Lenth);
	t_b = Quick_sort(t_b, t_b_Lenth);
	//병합과정
	t_a.push_back(pivot);
	for (int i = 0; i < t_b_Lenth; i++)
	{
		t_a.push_back(*t_b.begin());
		t_b.pop_front();
	}
	return t_a;
}

int main()
{
	list<int> a;
	int lenth = 0;
	cin >> lenth;
	int t;
	for (int i = 0; i < lenth; i++)
	{
		cin >> t;
		a.push_back(t);
	}
	a = Quick_sort(a, lenth);
	for (int i = 0; i < lenth; i++)
	{
		cout << *a.begin() << endl;
		a.pop_front();
	}
	return 0;
}