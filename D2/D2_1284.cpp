#include <iostream>
#include <algorithm>
using namespace std;
//수도 요금 경쟁
int main() {
	int len, p, q, r, s, w, result[2]{0};
	cin >> len;
	for (int l = 1; l <= len; l++) {
		cin >> p >> q >> r >> s >> w;
		result[0] = p * w;
		if (w <= r)	result[1] = q;
		else	result[1] = s * (w-r) + q;
		cout << "#" << l << " ";
		cout << min(result[0], result[1]) << endl;
	}
	return 0;
}