#include <iostream>
#include <string>
#include <cmath>

using namespace std;

int main()
{
	int a, b[19][19] = { 0 }, x, y;
	for (int i = 0; i < 19; i++)
	{
		for (int j = 0; j < 19; j++)
		{
			cin >> b[i][j];
		}
	}
	cin >> a;
	for (int i = 0; i < 2; i++)
	{
		cin >> x >> y;
		for (int j = 0; j < 19; j++)
		{
			if (j != x - 1)
			{
				b[x - 1][j] = !b[x - 1][j];
			}
			if (j != y - 1)
			{
				b[j][y - 1] = !b[j][y - 1];
			}

		}
	}
	for (int i = 0; i < 19; i++)
	{
		for (int j = 0; j < 19; j++)
		{
			cout << b[i][j] << " ";
		}
		cout << endl;
	}

	return 0;
}
