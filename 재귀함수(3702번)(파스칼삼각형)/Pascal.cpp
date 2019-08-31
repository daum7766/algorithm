#include <iostream>
using namespace std;

int pa[51][51];

int Recursion(int r, int c)
{
	if (pa[r][c])//값에 데이터가 있다면
	{
		return pa[r][c];
	}
	if (r == 1 || c == 1)	//기본조건 제일 위줄 혹은 왼쪽줄은 1
	{
		return 1;
	}
	return pa[r][c] = (Recursion(r - 1, c) + Recursion(r, c - 1)) % 100000000;

}


int main()
{
	int r;
	int c;
	cin >> r >> c;
	cout << Recursion(r, c) << endl;
	return 0;
}