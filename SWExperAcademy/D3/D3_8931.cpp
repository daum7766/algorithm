#include <iostream>
#include <stack>
using namespace std;
//D3 8931 제로

int main() {
	int len;
	cin >> len;
	//입력받은 횟수만큼 반복
	for (int l = 1; l <= len; l++) {
		//뒤에서 제거하므로 스택을 이용
		stack<int> st;
		int T, num, sum = 0;
		cin >> T;
		//입력 횟수만큼 반복
		for (int i = 0; i < T; i++) {
			cin >> num;
			//값이 0이 아니라면 스택에 추가
			if (num)	st.push(num);
			//0이라면 스택에서 데이터 제거
			else	st.pop();
		}
		// 스택이 빌때까지 반복한다.
		while (!st.empty()) {
			//스택의 내용을 sum에 더해준다.
			sum += st.top();
			//더해준 값을 뺀다.
			st.pop();
		}
		cout << "#" << l << " " << sum << endl;
	}
	return 0;
}