#include <string>
#include <iostream>
#include <cmath>

using namespace std;

//다음 문자열 확인함수
int nextCheck(string& dartResult, int i) {
	//인덱스가 길이를 넘지않는지 확인
	if (i + 1 < dartResult.length())
		switch (dartResult[i + 1]) {
		case '*':	return 2;	//스타상이라면 2배
		case '#':	return -1;		//아차상이라면 -1배
		}
	return 1;	//아무것도 아니라면 1배
}

int solution(string dartResult) {
	int current = 0, Squared = 0, score[3]{ 0, 0, 0 };
	//문자열을 처음부터 끝까지 반복
	for (int i = 0; i < dartResult.length(); i++) {
		//몇 제곱인지 확인
		if (dartResult[i] == 'S')	Squared = 1;
		else if (dartResult[i] == 'D')	Squared = 2;
		else if (dartResult[i] == 'T')	Squared = 3;
		//점수가 확인되었다면
		if (Squared) {
			//앞의 숫자 확인하기 1~10;
			int temp_int = stoi(dartResult.substr(0, i));
			//다음글자를 확인해서 2배인지 -1배인지 1배인지 확인
			int mulityply = nextCheck(dartResult, i);
			//1배가 아니라면 -> 2배 혹은 -1배라면
			if (mulityply != 1) {
				// -2배의 경우가 있을 수 있기때문에 다음것을 다시체크
				int temp = nextCheck(dartResult, i + 1);
				//둘중하나라도 2배라면 이전값도 2배로 바꾸기
				if ((mulityply == 2 || temp == 2) && current) 	score[current - 1] *= 2;
				//다음값이 1배가 아니라면 -> 즉 -2배라면
				if (temp != 1) {
					//제한사항7번인 *#이 중첩된경우이다.
					dartResult = dartResult.substr(i + 3);
					//-2배로 바꾸어준다
					mulityply *= temp;
				}
				//옵션이 1개이므로 2칸뒤로 이동한다.
				else	dartResult = dartResult.substr(i + 2);
			}
			//옵션이 없으므로 1칸뒤로 이동한다.
			else	dartResult = dartResult.substr(i + 1);
			//현재 다트횟수에 점수를 넣어준다.
			score[current] = pow(temp_int, Squared) * mulityply;
			//문자열을 잘랐으므로 인덱스초기화, 다트회수증가,  S D T영역 초기화
			i = 0;	Squared = 0;  current++;
		}
	}
	return score[0] + score[1] + score[2];
}


void print(string dartResult, int answer) {
	int t = solution(dartResult);
	if (answer == t)	cout << "정답" << endl;
	else	cout << "틀림" << endl;
}

int main() {
	print("1S2D*3T", 37);
	print("1D2S#10S", 9);
	print("1D2S0T", 3);
	print("1S*2T*3S", 23);
	print("1D#2S*3S", 5);
	print("1T2D3D#", -4);
	print("1D2S3T*", 59);

	return 0;
}
