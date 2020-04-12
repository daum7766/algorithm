#include <iostream>
#include <vector>
using namespace std;
//D2 1959 두개의 숫자열
int main() {
	//전체 반복횟수
	int len;
	cin >> len;
	for (int l = 1; l <= len; l++) {
		int a, b;
		long long max = 0;
		cin >> a >> b;
		vector<int> arr1(a), arr2(b), lo, sh;
		//a,b번만큼 반복하여 입력받기
		for (int i = 0; i < a; i++) cin >> arr1[i];
		for (int i = 0; i < b; i++)	cin >> arr2[i];
		//둘중 큰리스트를 찾아서 위치바꾸기
		if (arr1.size() >= arr2.size()) {
			lo = arr1;
			sh = arr2;
		}
		else {
			lo = arr2;
			sh = arr1;
		}
		//길이의 차이만큼 반복
		//옆으로 이동하면서 계산하며 제일 큰수를 찾는다.
		for (int i = 0; i <= lo.size() - sh.size(); i++) {
			long long temp = 0;
			for (int j = 0; j < sh.size(); j++) temp += lo[j + i] * sh[j];
			if (max < temp)	max = temp;
		}
		cout << "#" << l << " " << max << endl;
	}
	return 0;
}