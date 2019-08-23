#include  <iostream>
#include <list>

using namespace std;

list<int> a;
int lenth = 0;
//퀵정렬 함수
list<int> Quick_sort(list<int> b)
{
	//재귀함수 리턴조건
	if (b.size() <= 1)
	{
		return b;
	}
	//기준점 설정
	int pivot = *b.begin();
	b.pop_front();
	int t_lenth = b.size();
	//임시변수
	list<int> t_a;
	list<int> t_b;
	//크기 비교후 분할
	for (int i = 0; i < t_lenth; i++)
	{
		if (pivot >= *b.begin())
		{
			t_a.push_back(*b.begin());
			b.pop_front();
		}
		else
		{
			t_b.push_back(*b.begin());
			b.pop_front();
		}
	}
	//재귀함수 호출
	t_a = Quick_sort(t_a);
	t_b = Quick_sort(t_b);
	//정렬된 값 합치기
	t_a.push_back(pivot);
	t_lenth = t_b.size();
	for (int i = 0; i < t_lenth; i++)
	{
		t_a.push_back(*t_b.begin());
		t_b.pop_front();
	}
	//정렬된 결과값 반환
	return t_a;
}

int main()
{
	cin >> lenth;
	int t;
	for (int i = 0; i < lenth; i++)
	{
		cin >> t;
		a.push_back(t);
	}
	a = Quick_sort(a);
	for (int i = 0; i < lenth; i++)
	{
		cout << *a.begin() << endl;
		a.pop_front();
	}
	return 0;
}
