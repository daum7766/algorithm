#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

vector<int> solution(vector<int> array1, vector<vector<int>> commands) {
	vector<int> answer;

	//시작좀
	int start;
	//끝나는점
	int end;
	//찾아야하는 번호
	int index;
	//반환되야되는 세트동안 반복
	for (int i = 0; i < commands.size(); i++)
	{
		//임시 벡터 생성
		vector<int> temp;
		//필요한 조건변수 할당
		start = commands[i][0] - 1;
		end = commands[i][1];
		index = commands[i][2] - 1;
		//필요한 부분만 임시벡터에 넣음
		for (int j = start; j < end; j++)
		{
			temp.push_back(array1[j]);
		}
		//임시 벡터정렬
		sort(temp.begin(), temp.end());
		//임시벡터의 index번째를 answer에 넣음
		answer.push_back(temp.at(index));
	}

	return answer;
}

int main()
{
	int arr[] = { 1, 5, 2, 6, 3, 7, 4 };
	int arr2[][3] = { {2, 5, 3},{4, 4, 1},{1, 7, 3} };
	vector<int> temp;
	vector<vector<int>> temp2;
	for (int i = 0; i < 7; i++)
	{
		temp.push_back(arr[i]);
	}
	for (int i = 0; i < 3; i++)
	{
		vector<int> t;
		for (int j = 0; j < 3; j++)
		{
			t.push_back(arr2[i][j]);
		}
		temp2.push_back(t);
	}

	vector<int> result = solution(temp, temp2);
	for (int i = 0; i < result.size(); i++)
	{
		cout << result.at(i) << " ";
	}
	return 0;
}