#include <iostream>
#include <string>

using namespace std;
//D2 1979 어디에 단어가 들어갈 수 있을까
int main() {
    //퍼즐의 최대크기는 15이므로 15*15로 만들어 준다.
	int length, n, k, list[15][15];
	cin >> length;
    //전체반복횟수 test case만큼
	for (int i = 1; i <= length; i++) {
		cin >> n >> k;
		int answer = 0;
        //퍼즐상태를 입력받는다.
		for (int j = 0; j < n; j++) {
			int count = 0;
			for (int z = 0; z < n; z++)
				cin >> list[j][z];
		}
        //x와 y축을 돌면서 계산한다.
		for (int j = 0; j < n; j++) {
			int count1 = 0, count2 = 0;
			for (int z = 0; z < n; z++) {
                //값을 넣을수있다면 카운트
				if (list[z][j])      count1++;
                //값을 넣을수 없다면 체크한다.
				else {
                    //원하는 크기만큼 넣을수 있다면 answer증가
					if (count1 == k)       answer++;
                    //측정하는 변수 초기화
					count1 = 0;
				}
                //위와 동일하다.
				if (list[j][z])    count2++;
				else {
					if (count2 == k)      answer++;
					count2 = 0;
				}
			}// for z end
            //마지막부분까지 넣을수있었다면 체크해야한다.
            // 마지막 뒷부분이 k만큼인지 체크하여 answer 증가
			if (count1 == k)       answer++;
			if (count2 == k)      answer++;
		}// for j end
		cout << "#" << i << " " << answer << endl;
	}// for i end
	return 0;
}