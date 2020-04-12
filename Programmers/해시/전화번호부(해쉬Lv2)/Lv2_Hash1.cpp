#include <string>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

//hash 사용안함
//hash 문제인데 사용을 안하다니...
bool solution(vector<string> phone_book) {
	bool answer = true;
	//비교하기 쉽게 정렬
	sort(phone_book.begin(), phone_book.end());
	//처음부터 끝까지 순회
	for (int i = 0; i < phone_book.size() - 1; i++){
		//i보다 뒷부분만 순회
		for (int j = i + 1; j < phone_book.size(); j++){
			//정렬이 되어있기때문에 길이비교 하지않음
			//비교하는 부분이 일치한다면 false 리턴
			if (phone_book[i] == phone_book[j].substr(0, phone_book[i].length()))
				return false;
		}
	}
	return answer;
}


int main()
{
	string a[] = { "119", "97674223", "1195524421" };
	vector<string> b;
	for (int i = 0; i < 3; i++)
	{
		b.push_back(a[i]);
	}
	cout << solution(b) << endl;
	return 0;
}