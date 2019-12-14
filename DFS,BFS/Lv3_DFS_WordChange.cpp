#include <string>
#include <vector>
#include <iostream>
using namespace std;
int answer{ 100 };
//시작단어, 목표단어, 단어리스트, 단어리스트사용여부, 목표까지 들어간 횟수(깊이)
void dfs(string begin, string target, vector<string> words, vector<bool>& useCheck, int cnt = 0) {
	//단어의 사이즈만큼 반복
	for (int i = 0; i < words.size(); i++) {
		//알파벳끼리 일치여부 초기화
		int count{ 0 };
		//한글자씩 비교하면서 글자가 다를경우 카운트 증가
		for (int j = 0; j < words[j].length(); j++)
			if (!useCheck[i] && begin[j] != words[i][j])	count++;
		//카운트가 1이라면(한 글자만 다른경우)
		if (count == 1) {
			//1글자만 다른 단어가 target단어이고 answer가 지금까지 들어온 깊이+1보다 큰경우 answer변경
			if (target == words[i] && answer > cnt + 1) {
				answer = cnt + 1;
				return;
			}
			//단어를 사용했다 체크하고 재귀
			useCheck[i] = true;
			dfs(words[i], target, words, useCheck, cnt + 1);
			//함수를 나온경우 단어사용여부 해제
			useCheck[i] = false;
		}
	}
}

int solution(string begin, string target, vector<string> words) {
	//사용한 단어 체크용(words의 길이만큼 생성하고 fasle로 초기화한다.)
	vector<bool> useCheck(words.size(), false);
	dfs(begin, target, words, useCheck);
	//answer가 100이면 target까지 갈수없으므로 0을 리턴한다.
	if (answer == 100)   return 0;
	//위조건이 무시된다면 target까지 제일짧은 횟수를 리턴
	return answer;
}

void print(string begin, string target, vector<string> words, int answer) {
	::answer = 100;
	int t = solution(begin, target, words);
	cout << t << " , ";
	if (t == answer)		cout << "정답" << endl;
	else		cout << "틀림" << endl;
}

int main() {
	print("hit", "cog", { "hot", "dot", "dog", "lot", "log", "cog" }, 4);
	print("hit", "cog", { "hot", "dot", "dog", "lot", "log" }, 0);
	print("hot", "lot", { "dot", "dog", "lot", "log" }, 1);
	print("hit", "wow", { "hot", "dot", "dog", "lot", "log", "cog", "wow" }, 0);
	return 0;
}