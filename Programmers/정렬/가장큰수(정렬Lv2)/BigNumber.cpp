#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

//합친 문자 비교해서 큰순으로 정렬하기, ex ) 6, 10 이 있다면 610과 106하고 어떤게 큰지 비교
// 610이 더크므로 6, 10순으로 정렬하게 된다.
bool cmp(string a, string b){
	return a + b > b + a;
}

string solution(vector<int> numbers) {
	string answer = "";
	vector<string> temp;
	//string으로 바꾼후 벡터에 집어넣는다.
	for (auto num : numbers)
		temp.push_back(to_string(num));
	//더할때 오름차순으로 정렬한다.
	sort(temp.begin(), temp.end(), cmp);
	//처음 숫자가 0이라면 0을 반환
	if (temp.at(0) == "0")		return "0";
	//처음부터 끝까지 문자열 합치고 리턴
	for (auto num : temp)
		answer += num;
	return answer;
}

void print(vector<int> numbers, string answer) {
	string t = solution(numbers);
	if (t == answer)
		cout << "정답" << endl;
	else
		cout << "틀림" << endl;
}

int main(){
	print({6, 10, 2}, "6210");
	print({ 3, 30, 34, 5, 9 }, "9534330");
	print({ 0,0,0,0,0,0,0 }, "0");

	return 0;
}