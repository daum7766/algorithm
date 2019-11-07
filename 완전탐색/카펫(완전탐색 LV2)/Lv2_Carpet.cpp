#include <iostream>
#include <vector>

using namespace std;

vector<int> solution(int brown, int red) {
	vector<int> answer;
	int sum = brown + red;
	for (int height = 3; ; height++) {
		if (sum % height == 0) {
			int weight = sum / height;
			//테두리는 갈색이므로 2줄씩 빼고 계산
			if (((height - 2) * (weight - 2)) == red) {
				answer.push_back(weight);
				answer.push_back(height);
				break;
			}
		}
	}
	return answer;
}

void print(int b, int r)
{
	for (auto a : solution(b, r))
	{
		cout << a << " ";
	}
	cout << endl;
}

int main() {

	print(10, 2);
	print(8, 1);
	print(24, 24);
	return 0;
}