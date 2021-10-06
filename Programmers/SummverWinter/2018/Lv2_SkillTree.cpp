#include <string>
#include <vector>
#include <iostream>
#include <map>

using namespace std;


int solution(string skill, vector<string> skill_trees) {
	int answer = 0;
	map<char, int> tree;
	//�ؽ��ʿ� ��ų������ ����
	for (int i = 0; i < skill.length(); i++)
		tree[skill[i]] = i + 1;
	//��ųƮ�� ��ȸ�ϱ�
	for (auto skt : skill_trees) {
		int count = 1;
		bool check = true;
		//���� ��ų�� ��ųƮ���� ����Ǵ��� Ȯ��
		for (int i = 0; i < skt.length(); i++) {
			//��ų������ �����ʴٸ� Ż��
			if (tree[skt[i]] > count) {
				check = false;
				break;
			}
			//�ּ� ��ųƮ���� �����ٸ� ������ų�� �������ֵ��� ����
			else if (tree[skt[i]] == count)
				count++;
		}
		//�̻��� ����ߴٸ� ��� ��ų�� ���������Ƿ� ī��Ʈ ����
		if (check)
			answer++;
	}
	return answer;
}

void print(string skill, vector<string> skill_trees, int answer) {
	int t = solution(skill, skill_trees);
	//cout << t << " , ";
	if (answer == t)
		cout << "����" << endl;
	else
		cout << "Ʋ��" << endl;
}

int main() {
	print("CBD", { "BACDE", "CBADF", "AECB", "BDA" }, 2);
	return 0;
}
