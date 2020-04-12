#include <iostream>
#include <string>
#include <cmath>

using namespace std;

int main()
{
	int w, h, n, l, d, x, y;
	cin >> w >> h;
	int **t = new int *[w];
	for (int i = 0; i < w; i++)
	{
		t[i] = new int[h];
		for (int j = 0; j < h; j++)
		{
			t[i][j] = 0;
		}
	}
	cin >> n;
	for (int i = 0; i < n; i++)
	{
		cin >> l >> d >> x >> y;
		if (d == 0)		//가로일때
		{
			for (int i = 0; i < l; i++)
			{
				t[x - 1][y - 1 + i] = 1;
			}

		}
		else		//세로일때
		{
			for (int i = 0; i < l; i++)
			{
				t[x - 1 + i][y - 1] = 1;
			}
		}


	}
	for (int i = 0; i < w; i++)
	{
		for (int j = 0; j < h; j++)
		{
			cout << t[i][j] << " ";
		}
		cout << endl;
	}
	for (int i = 0; i < w; i++)
	{
		delete[] t[i];
	}
	delete[] t;

	return 0;
}
