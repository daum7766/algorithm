#include <string>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

vector<int> tempList;

//�Ҽ� �Ǻ� �Լ�
bool Decheck(int a) {
	for (int i = 2; i <= sqrt(a); i++)
		if (a % i == 0)//i�� ����������� �Ҽ��� �ƴ� 
			return false;
	return true;
}
//����Ǽ� ��ġ��(����Լ�, ���̴� 3�̻� ���� ����)
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
	//����Ǽ� �����
	for (int i = 0; i < nums.size() - 2; i++)
		serch(nums, i);
	//���� ������ �Ҽ����� �Ǵ�
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
		cout << "����" << endl;
	else
		cout << "Ʋ��" << endl;
}

int main() {
	print({ 1,2,3,4 }, 1);
	print({ 1,2,7,6,4 }, 4);

	return 0;
}
