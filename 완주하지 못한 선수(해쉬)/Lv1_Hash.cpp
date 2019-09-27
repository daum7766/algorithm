#include <vector>
#include <string>
#include <unordered_map>//해쉬맵 사용
#include <iostream>//메인 출력용
#include <algorithm>//솔루션 2용
using namespace std;

//해쉬테이블을 이용한 솔루션
string solution(vector<string> participant, vector<string> completion)
{
	string answer = "";
	unordered_map<string, int> temp;
	for (string name : participant)
	{
		//해쉬테이블에 key값으로 name을 주고 값을 더함
		temp[name]++;
	}
	for (string name : completion)
	{
		//name key로 접근하여 값을 감소
		temp[name]--;
	}
	//처음부터 해쉬테이블 순회
	for (auto pair : temp)
	{
		//해쉬테이블의 2번째값이 0보다 크다면
		if (pair.second > 0)
		{
			//answer에 해쉬테이블 key값을 넣음
			answer = pair.first;
			break;
		}
	}
	return answer;
}

//정렬을 이용한 솔루션
string solution2(vector<string> participant, vector<string> completion)
{
	//참가자와 완주자 리스트를 정렬
	sort(participant.begin(), participant.end());
	sort(completion.begin(), completion.end());
	//완주자 리스트 순회
	for (int i = 0; i < completion.size(); i++)
	{
		//참가자가 완주자 이름이 다르다면
		if (participant[i] != completion[i])
		{
			//다른 이름값을 리턴
			return participant[i];
		}
	}
	//위의 조건에 걸리지 않았다면 참가자중 제일 마지막값 리턴
	return participant[participant.size() - 1];
}

int main() {
	vector<string> a, b;
	string a1[] = { "marina", "josipa", "nikola", "vinko", "filipa" };
	string a2[] = { "josipa", "filipa", "marina", "nikola" };

	for (int i = 0; i < 5; i++)
	{
		a.push_back(a1[i]);
	}
	for (int i = 0; i < a.size() - 1; i++)
	{
		b.push_back(a2[i]);
	}
	cout << solution(a, b) << endl;
	return 0;
}