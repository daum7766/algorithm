#include <iostream>
#include <string>
#include <cmath>

using namespace std;

int main()
{
	int t[10][10];
	int x = 1, y = 1;

	for (int i = 0; i < 10; i++)
	{
		for (int j = 0; j < 10; j++)
		{
			cin >> t[i][j];
		}
	}
	while (true)
	{
		if (t[x][y] == 2)
		{
			t[x][y] = 9;
			break;
		}
		t[x][y] = 9;
		if (t[x][y + 1] == 0 || t[x][y + 1] == 2)
		{
			y++;
			continue;
		}
		if (t[x + 1][y] == 0 || t[x + 1][y] == 2)
		{
			x++;
			continue;
		}

		if (t[x][y + 1] == 1 && t[x + 1][y] == 1)
		{
			break;
		}
	}
	for (int i = 0; i < 10; i++)
	{
		for (int j = 0; j < 10; j++)
		{
			cout << t[i][j] << " ";
		}
		cout << endl;
	}

	return 0;
}
