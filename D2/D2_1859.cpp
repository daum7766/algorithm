#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
	int length, m_length, t, count = 1;
	//총 반복할 횟수
	cin >> length;
	while (length--) {
		//내부 입력받는 횟수
		cin >> m_length;
		//벡터에 리스트를 저장
		vector<int> list;
		//
		long long answer = 0;
		//모든 입력을 vector에 추가
		while (m_length--) {
			cin >> t;
			list.push_back(t);
		}
		//기준이 될값을 저장(벡터의 제일 마지막부분)
		int max = *--list.end();
		//벡터의 마지막 전부터 처음까지 반복한다.
		for (int i = list.size() - 2; i >= 0; i--) {
			//기준값보다 적을경우 이득추가
			if (list[i] <= max)      	answer += max - list[i];
			//아니라면 기준값 변경
			else      max = list[i];
		}
		cout << "#" << count++ << " " << answer << endl;
	}
	return 0;
}