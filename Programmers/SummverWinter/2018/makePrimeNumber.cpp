#include <string>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

vector<int> tempList;

//소수 판별 함수
bool Decheck(int a) {
	for (int i = 2; i <= sqrt(a); i++)
		if (a % i == 0)//i가 나누어떨어지면 소수가 아님 
			return false;
	return true;
}
//경우의수 서치용(재귀함수, 깊이는 3이상 가지 않음)
void serch(vector<int>& nums, int index = 0, int count = 0, int sum = 0) {
	if (index >= nums.size())
		return;
	sum += nums[index];
	for (int i = index; i < nums.size(); i++) {
		if (count == 2) {
			tempList.push_back(sum);
			return;
		}
		else
			serch(nums, i + 1, count + 1, sum);
	}
}

int solution(vector<int> nums) {
	int answer = 0;
	//경우의수 만들기
	for (int i = 0; i < nums.size() - 2; i++)
		serch(nums, i);
	//나온 수들이 소수인지 판단
	for (auto a : tempList) {
		if (Decheck(a))
			answer++;
	}
	return answer;
}

void print(vector<int> nums, int answer) {
	int t = solution(nums);
	cout << t << " , ";
	if (answer == t)
		cout << "정답" << endl;
	else
		cout << "틀림" << endl;
}

int main() {
	print({ 1,2,3,4 }, 1);
	print({ 1,2,7,6,4 }, 4);

	return 0;
}
