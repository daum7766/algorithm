#include <vector>
#include <iostream>
#include <string>

using namespace std;


string solution(string number, int k) {
	string answer = "";
	int t = number.length() - k;
	//필요한 글자수만큼 반복하기
	for (int j = t; j > 0; j--) {
		int index = 0;
		char max = 0;
		//앞에서 남겨야 되는 숫자 중에 제일 큰수 체크
		for (int i = 0; i <= number.length() - j; i++) {
			if (max < number[i]) {
				index = i;
				max = number[i];
			}
		}
		//제일 큰수를 정답에 추가하고
		answer += max;
		//수를 뽑은부분만큼 지우기
		number.replace(0, index + 1, " ");
	}
	return answer;
}


void print(string number, int k, string answer)
{
	string t = solution(number, k);
	cout << t << " ";
	if (t == answer)
		cout << "정답" << endl;
	else
		cout << "틀림" << endl;

}


int main() {
	print("9999", 2, "99");
	print("1924" , 2, "94");
	print("1231234", 3, "3234");
	print("4177252841", 4, "775841");


	return 0;
}