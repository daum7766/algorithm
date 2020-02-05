#include <iostream>

using namespace std;

int main(){
    //반복길이와 돈, 한국돈을 입력
	int length, money, Kmoney[8]{50000, 10000, 5000, 1000, 500, 100, 50, 10};
    cin >> length;
    //길이만큼 반복
    for(int l = 1; l<=length; l++){
        cin >> money;
        cout << "#"<<l<<endl;
        //입력받은 돈을 제일 앞의수부터 나누어준다.
        for(int i=0; i<8; i++){
        	cout << (money / Kmoney[i]) << " ";
            //나머지 연산을 통해 돈의 액수를 줄인다.
            money %= Kmoney[i];
        }
        cout << endl;
    }
    
    return 0;
}