#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

long long solution(int n, vector<int> times) {
	//����, �ּҽð�, �ִ�ð�, ��սð�
	long long answer = 0, minTime = 1, maxTime, avgTime, human = 0;
	//�ִ밪 �� �ִ��ο��� * �ο���
	maxTime = *max_element(times.begin(), times.end()) * (long long)n;
	//�ּҽð��� �ִ�ð��� ���ų� ���������� �ݺ�
	while (minTime <= maxTime) {
		//��սð� ���ϱ�
		avgTime = ((maxTime + minTime) / 2);
		//���� �ð����� ������ �մ� �ִ��ο� ���ϱ�
		for (auto t : times)		human += avgTime / t;
		//�ִ��ο��� ���ο����� ũ�ų� ���ٸ�
		if (n <= human) {
			//���� �ð��� ���信 ����(���߿� �ȳ����� �����ؾ� �ؼ�
			answer = avgTime;
			//�ִ�ð� ����
			maxTime = avgTime - 1;
		}
		//���ο����� ���ٸ� ���纸�� �ð���Ŀ���ϹǷ� �ּҽð� ����
		else	minTime = avgTime + 1;
		//����� �ʱ�ȭ
		human = 0;
	}
	return answer;
}

void print(int n, vector<int> times, long long answer){
	long long t = solution(n, times);
	if (t == answer)		cout << "����" << endl;
	else		cout << "Ʋ��" << endl;
}

int main(){
	print(6, { 7, 10 }, 28);
	print(1, { 2, 2 }, 2);
	print(1, { 1 }, 1);
	return 0;
}