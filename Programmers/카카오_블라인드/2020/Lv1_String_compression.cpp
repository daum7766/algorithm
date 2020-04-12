#include <string>
#include <iostream>

using namespace std;

int solution(string s) {
	int answer = s.length();
	//경우의 수 탐색하기
	for (int i = 1; i <= s.length() / 2; i++) {
		int len = s.length();
		//문자열을 전체 돌면서 반복
		for (int j = 0; j < s.length(); j++) {
			//부분 비교하기
			for (int count = 0, z = i; j + z < s.length(); z += i) {
				//뒤부분과 일치한다면 count 증가
				if (s.substr(j, i) == s.substr(j + z, i))    count++;
				//뒤에부분이 일치하지않는다면 count확인후 중복되는 문자열만큼 길이줄임
				//추가되는 숫자만큼 길이증가
				else {
					len -= i * count;
					if (count) 	len += to_string(count + 1).length();
					j += z - 1;
					break;
				}
				// 한번이라도 압축이 된상태에서 뒤에가 계산이 안된다면
				//압축후 추가하고 나머지를 뒤에 추가
				if (j + z + i >= s.length()) {
					len -= i * count;
					len += to_string(count + 1).length();
					j += z;
				}
			}
		}
		//문자열 길이를 비교해서 적어진다면 적은걸로 변경
		if (len < answer)	answer = len;
	}
	return answer;
}


void print(string s, int answer) {
	int t = solution(s);
	if (answer == t)
		cout << "정답" << endl;
	else
		cout << "틀림" << endl;
}


int main() {
	print("a", 1);
	print("aaaaa", 2);
	print("aaaaaaaaaa", 3);
	print("aabbaccc", 7);
	print("ababcdcdababcdcd", 9);
	print("abcabcdede", 8);
	print("abcabcabcabcdededededede", 14);
	print("xababcdcdababcdcd", 17);
	return 0;
}
