#include <string>
#include <vector>
#include <iostream>

using namespace std;

vector<string> solution(int n, vector<int> arr1, vector<int> arr2) {
	vector<string> answer;
	//0이면 빈칸을 1이면 #을 넣는용
	char list[2]{ ' ', '#' };
	//or연산을 담아두는 임시 리스트
	vector<int> temp_arr;
	//배열은 순회하면서 or연산
	for (int i = 0; i < arr1.size(); i++)
		temp_arr.push_back(arr1[i] | arr2[i]);
	//연산된 값을 2로 나누면서 n만큼 푸시하기
	for (auto temp : temp_arr) {
		string s_temp = "";
		int count = 0;
		while (++count <= n) {
			s_temp = list[temp & 1] + s_temp;
			temp /= 2;
		}
		answer.push_back(s_temp);
	}

	return answer;
}

void print(int n, vector<int> arr1, vector<int> arr2, vector<string> answer) {
	vector<string> t = solution(n, arr1, arr2);
	for (auto a : t)
		cout << a << " , ";
	if (answer == t)
		cout << "정답" << endl;
	else
		cout << "틀림" << endl;
}

int main() {
	print(6, { 46, 33, 33, 22, 31, 50 }, { 27, 56, 19, 14, 14, 10 }, { "######", "###  #", "##  ##", " #### ", " #####", "### # " });
	print(5, { 9, 20, 28, 18, 11 }, { 30, 1, 21, 17, 28 }, { "#####", "# # #", "### #", "#  ##", "#####" });
	return 0;
}