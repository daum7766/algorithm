#include <iostream>
#include <string>

using namespace std;
//D2 1976 시각덧셈
int main(){
    int length;
    cin >> length;
    //테스트 케이스만큼 반복
    for(int i=1; i<=length; i++){
        //시간과 분, 분의합을 위한 변수
        int h1, h2, h3= 0, m1, m2, m3 = 0, sum = 0;
        cin >> h1 >> m1 >> h2 >>m2;
        //모든 시간을 분으로 바꾸어 처리한다.
        sum = h1*60 + m1 + h2*60 + m2;
        //분을 시간으로 바꾼다.
        h3 = (sum/60) %12;
        //남은 분을 계산한다.
        m3 = sum%60;
        //0시 라면 12시로 바꿔주기
        if(!h3) h3 = 12;
    	cout << "#" << i << " " <<h3 <<" " <<m3 << endl;
    }
	return 0;
}