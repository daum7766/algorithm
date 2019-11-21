#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <map>

using namespace std;
int list[9][9];

int nextCheck() {
	map<int, int> check;
	for (int i = 0; i < 9; i += 3) {
		for (int j = 0; j < 9; j += 3) {
			for (int k = i; k < i + 3; k++) {
				for (int y = j; y < j + 3; y++) {
					if (check[list[k][y]])		return 0;
					check[list[k][y]]++;
				}
			}
			check.clear();
		}
	}
	return 1;
}

int solution() {
	map<int, int> check1, check2;
	for (int i = 0; i < 9; i++) {
		for (int j = 0; j < 9; j++)
			cin >> list[i][j];
	}
	for (int i = 0; i < 9; i++) {
		for (int j = 0; j < 9; j++) {
			if (check1[list[i][j]] || check2[list[j][i]])	return 0;
			check1[list[i][j]]++;
			check2[list[j][i]]++;
		}
		check1.clear();
		check2.clear();
	}
	return nextCheck();
}

int main() {
	int length;
	cin >> length;
	for (int l = 1; l <= length; l++)
		cout << "#" << l << " " << solution() << endl;
	return 0;
}