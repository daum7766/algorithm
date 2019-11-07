#include <vector>
#include <string>
#include <iostream>//메인 출력용
#include <algorithm>
#include <set>
using namespace std;

//경우의 수 찾기용, 경우의 수 담기용, 문자열 합치기용
void push(vector<pair<char, bool>> piece, set<int>& p, string a = "", int cnt = 0) {
	//처음붙터 끝까지 반복문을 돌린다.
	for (int j = 0; j < piece.size(); j++) {
		//j인덱스에 관련된 piece가 사용중이지 않다면
		if (!piece.at(j).second) {
			//사용중으로 변경
			piece.at(j).second = true;
			//문자열 추가
			a += piece.at(j).first;
			//현재 문자열을 경우의 수에 담기
			p.insert(atoi(a.c_str()));
			cnt++;
		}
		else//사용중이라면 위로 보내기
			continue;
		//모두 사용중이 아니라면 재귀
		if (cnt != piece.size())	push(piece, p, a, cnt);
		//사용을 완료하면 사용하지 않음으로 바꾸기
		piece.at(j).second = false;
		//돌아가기 전에 문자열을 하나 감소
		a = a.substr(0, a.length() - 1);
		cnt--;
	}
}

bool Decheck(int a) {
	for (int i = 2; i <= sqrt(a); i++)
		if (a % i == 0)//i가 나누어떨어지면 소수가 아님 
			return false;
	return true;
}

int solution(string numbers) {
	int answer = 0;
	//모든 경우의 수를 찾기 위한 용도
	vector<pair<char, bool>> piece;
	//모든 경우의 수를 모으는 곳
	set<int> p;
	//반복문으로 numbers를 쪼개서 piece에 집어넣는다.
	for (int i = 0; i < numbers.length(); i++)
		piece.push_back(make_pair(numbers[i], false));
	//모든 경우의 수 찾기
	push(piece, p);
	for (auto c : p) {
		//0과 1인경우는 소수에서 제외
		if (c == 0 || c == 1)	continue;
		//소수를 체크해서 소수면 카운트 증가
		if (Decheck(c))		answer++;
	}
	return answer;
}

int main() {
	string a{ "011" };
	cout << solution(a) << endl;
	return 0;
}