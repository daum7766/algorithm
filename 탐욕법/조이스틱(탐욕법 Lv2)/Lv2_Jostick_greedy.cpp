#include <vector>
#include <iostream>
#include <string>

using namespace std;

int solution(string name) {
	int answer = 0;
	//조이스틱으로 바꾸고있는 화면
	vector<char> names(name.length(), 'A');
	//바뀌어야 하는 결과
	vector<char> temp;
	//temp에 name을 끊어서 집어넣기
	for (int i = 0; i < name.length(); i++)
		temp.push_back(name[i]);
	int i = 0;
	while (true) {
		//현재 서로 모양이 맞지 않는다면
		if (names.at(i) != temp.at(i)) {
			//바꾸고 있는 화면에 반영하고
			names.at(i) = temp.at(i);
			int a, b;
			//앞으로 바꿧을때 횟수
			a = temp.at(i) - 'A';
			//뒤로 바꿧을때 횟수
			b = 'Z' + 1 - temp.at(i);
			//둘중에 적은걸로 결과에 추가하기
			a > b ? answer += b : answer += a;
		}
		int left = 1, right = 1;
		bool check = true;
		//왼쪽으로 갈지 오른쪽으로 갈지 계산하기 
		while (true) {
			//인덱스를 넘지않게 나머지 계산
			int t = (i + right) % names.size();
			//오른쪽으로 이동하는 위치가 결과와 같다면 옆으로 한칸더
			if (names.at(t) == temp.at(t))
				right++;
			else//오른쪽으로 이동해서 바꿔야 한다면 정지
				break;
			//모든 문자가 똑같아서 right가 계속 올라가면 반복문 탈출
			if (right > name.size()) {
				check = false;
				break;
			}
		}
		//모든문자가 같지않을때만 동작
		if (check) {
			while (true) {
				//왼쪽으로 이동
				int t = i - left;
				//계산한 인덱스가 0보다 작다면 맞춰주기
				if (t < 0)	t = names.size() + t;
				//왼쪽으로 이동하는 위치가 결과와 똑같다면 옆으로 더이동
				if ((names.at(t) == temp.at(t)))
					left++;
				//문자가 다를때 정지
				else
					break;
			}
		}
		else//모든 문자가 같으면 모두 맞춰진것이므로 반복문 탈출
			break;
		//오른쪽으로 이동하는게 이득이라면
		if (right <= left) {
			//오른쪽으로 이동해야 하는만큼 이동하고
			i = (i + right) % names.size();
			//이동한 횟수만큼 결과에 반영
			answer += right;
		}
		else {//왼쪽으로 이동하는게 이득이라면
			//왼쪽으로 이동해야 하는만큼 이동하고
			i -= left;
			//인덱스를 넘어갔는지 확인하고 넘어가면 인덱스 보정
			if (i < 0)
				i += names.size();
			//이동한 횟수만큼 결과에 반영
			answer += left;
		}
	}
	return answer;
}


void print(string name, int answer)
{
	int a = solution(name);
	cout << a << " ";
	if (answer == a)
		cout << "정답" << endl;
	else
		cout << "틀림 " << endl;

}


int main() {

	print("JEROEN", 56);
	print("JAN", 23);
	print("AABAAAAAAAB", 6);
	print("AAAAAAAA", 0);
	print("ABBBBAAAABAA", 14);
	print("ABAAAAAAABA", 6);
	print("AAB", 2);
	print("AABAAAAAAABBB", 12);
	print("ZZZ", 5);

	return 0;
}