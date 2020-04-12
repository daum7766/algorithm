#include <iostream>
#include <algorithm>
using namespace std;
//수도 요금 경쟁
int main() {
	int len, p, q, r, s, w, result[2]{0};
	cin >> len;
	for (int l = 1; l <= len; l++) {
		//리터당요금, R리터 이하요금, 제한사용량, 초과분 리터당 요금, 수도 사용량
		cin >> p >> q >> r >> s >> w;
		//A사는 요금 * 사용량
		result[0] = p * w;
		//R이하만큼 사용했다면 사용량은 Q
		if (w <= r)	result[1] = q;
		//R초과라면 초과분만큼 추가한다.
		else	result[1] = s * (w-r) + q;
		cout << "#" << l << " ";
		//둘중 작은 값을 출력한다.
		cout << min(result[0], result[1]) << endl;
	}
	return 0;
}