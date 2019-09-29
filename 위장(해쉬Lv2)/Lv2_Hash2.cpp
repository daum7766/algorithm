#include <string>
#include <vector>
#include <iostream>
#include <unordered_map>//해쉬맵 사용

using namespace std;

int solution(vector<vector<string>> clothes) {
	//곱하기 연산을 해야하기때문에 기본값 1
	int answer = 1;
	unordered_map<string, int> temp;
	//큰 테두리로 분류(얼굴, 상의, 하의, 겉옷 등)
	for (int i = 0; i < clothes.size(); i++)
	{
		temp[clothes[i][1]]++;
	}
	//Hash를 처음부터 순회
	for (auto pair : temp)
	{
		//종류의 수 +1 (아무것도 입지않았을때) 를 계속 곱해준다.
		answer *= (pair.second + 1);
	}
	//무언가 하나는 입어야 하므로
	//아무것도 입지않은 경우의수 제외
	return answer - 1;
}



int main()
{
	string a[][2] = { {"yellow_hat", "headgear"},{"blue_sunglasses", "eyewear"},{"green_turban", "headgear"} };
	vector<vector<string>> b;
	for (int i = 0; i < 3; i++)
	{
		b.push_back(vector<string>());
		for (int j = 0; j < 2; j++)
		{
			b.at(i).push_back(a[i][j]);
		}

	}
	cout << solution(b) << endl;
	return 0;
}