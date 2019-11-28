#include <string>
#include <vector>

using namespace std;

string solution(string s) {
	s[0] = toupper(s[0]);
	for (int i = 1; i < s.length(); i++) {
		if (s[i - 1] == ' ')     s[i] = toupper(s[i]);
		else    s[i] = tolower(s[i]);
	}
	return s;
}

void print(string s, string answer){
	strint t = solution(s);
	if (t == answer)
		cout << "정답" << endl;
	else
		cout << "틀림" << endl;
}

int main() {
	print("3people unFollowed me", "3people Unfollowed Me");
	print("for the last week", "For The Last Week");
	return 0;
}