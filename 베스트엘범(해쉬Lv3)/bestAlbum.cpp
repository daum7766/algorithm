#include <string>
#include <vector>
#include <iostream>
#include <map>//해쉬맵 사용

using namespace std;

vector<int> solution(vector<string> genres, vector<int> plays) {
	vector<int> answer;
	//각 장르별로 횟수저장
	map<string, int> music;
	//각 장르별로 무슨노래가 몇번씩 저장됬는지
	map<string, map<int, int>> musiclist;
	//들어온 리스트만큼 반복
	for (int i = 0; i < genres.size(); i++) {
		//music map에 장르별로 횟수추가
		music[genres[i]] += plays[i];
		//musiclist map에 노래번호와 플레이횟수 추가
		musiclist[genres[i]][i] = plays[i];
	}
	//장르가 다없어질때까지 반복
	while (music.size() > 0) {
		string genre{};
		int max{ 0 };
		//장르중에서 제일높은것 찾기
		for (auto mu : music) {
			if (max < mu.second) {
				max = mu.second;
				genre = mu.first;
			}
		}
		//2곡을 넣어야하므로 2번반복
		for (int i = 0; i < 2; i++) {
			int val = 0, ind = -1;
			//노래중에서 제일높은것 찾기
			for (auto ml : musiclist[genre]) {
				if (val < ml.second) {
					val = ml.second;
					ind = ml.first;
				}
			}
			//만약 노래가 0~1곡밖에없다면 반복문 탈출
			if (ind == -1)	break;
			//리턴할 리스트에 노래번호 추가
			answer.push_back(ind);
			musiclist[genre].erase(ind);
		}
		//map 에서 사용한 장르삭제
		music.erase(genre);
	}
	return answer;
}



int main(){
	vector<string> genres{ "classic","pop","classic","pop","classic","classic" };
	vector<int> plays{ 400,600,150,2500,500,500 };
	vector<int> result = solution(genres, plays);
	for (int i = 0; i < result.size(); i++)
		cout << result.at(i) << endl;

	return 0;
}