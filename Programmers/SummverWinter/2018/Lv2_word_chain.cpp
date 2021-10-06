#include <string>
#include <vector>
#include <map>

using namespace std;

vector<int> solution(int n, vector<string> words) {
	map<string, int> word;
	word[words[0]]++;
	for (int i = 1; i < words.size(); i++) {
		if (word[words[i]] || words[i].front() != words[i - 1].back())
			return { (i % n) + 1,(i / n) + 1 };
		word[words[i]]++;
	}
	return { 0, 0 };
}

void print(int n, vector<string> words, vector<int> answer) {
	vector<int> t = solution(n, words);
	if (t == answer) cout << "정답" << endl;
	else	cout << "틀림" << endl;
}

void main() {
	print(3, { "tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank" }, {3, 3});
	print(5, { "hello", "observe", "effect", "take", "either", "recognize", "encourage", "ensure", "establish", "hang", "gather", "refer", "reference", "estimate", "executive" }, {0, 0});
	print(2, { "hello", "one", "even", "never", "now", "world", "draw" }, {1, 3});

	return 0;
}