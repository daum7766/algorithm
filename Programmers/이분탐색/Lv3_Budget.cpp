#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

int solution(vector<int> budgets, int M) {
	//����, �ִ밪, �ּڰ�, ���
	int answer = 0, max = 100000, min = 1, avg;
	while (min <= max) {
		//���Ѿ��� �����ʿ䰡 ������ üũ��
		bool check = true;
		long long sum = 0;
		avg = (max + min) / 2;
		//��ȸ�� �ϸ鼭 ���Ѿ׺��� ũ�ٸ� ��հ����� �ٲٰ� ����
		for (auto a : budgets) {
			if (a > avg) {
				sum += avg;
				check = false;
			}
			else	sum += a;
		}
		//������ �ִ� ������ �Ѿ��ٸ� �ִ밪�� �����ϰ� �ٽ� �ݺ�
		if (sum > M)	max = avg - 1;
		//������ �ִ� ������ ���� ������
		else {
			//���Ѿ׿� �ѹ��� �ɸ����ʾҴٸ� ������ �ִ� ����
			if (check)		return *max_element(budgets.begin(), budgets.end());
			//�װԾƴ϶�� �ּڰ� �ٲٰ� �ٽð��
			min = avg + 1;
			answer = avg;
		}
	}
	return answer;
}

void print(vector<int> budgets, int M, int answer){
	int t = solution(budgets, M);
	if (t == answer)	cout << "����" << endl;
	else	cout << "Ʋ��" << endl;
}

int main() {
	print({ 120, 110, 140, 150 }, 485, 127);
	print({ 1,2,3,4,5,6,7,8,9,10 }, 56, 10);
	return 0;
}