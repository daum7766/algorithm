#include <iostream>
#include <string>

using namespace std;
const static int MAX = 100;

struct student
{
	string name;
	int grade;
};
student students[MAX];

void Sort()
{
	bool check = true;
	for (int i = MAX - 1; i >= 0; i--)
	{
		for (int j = 0; j < i; j++)
		{
			if (students[j].grade < students[j + 1].grade)
			{
				check = false;
				student temp = students[j];
				students[j] = students[j + 1];
				students[j + 1] = temp;
			}
		}
		if (check)
		{
			break;
		}
		check = true;
	}
}

int main()
{
	int length, cut;
	cin >> length >> cut;
	string name;
	int grade;
	for (int i = 0; i < length; i++)
	{
		cin >> name >> grade;
		student temp;
		students[i].name = name;
		students[i].grade = grade;
	}
	Sort();
	for (int i = 0; i < cut; i++)
	{
		cout << students[i].name << endl;
	}

	return 0;
}