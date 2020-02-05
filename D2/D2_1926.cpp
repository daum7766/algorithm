
#include <iostream>
#include <string>

using namespace std;

//D2 1926 간단한 369게임

int main(){
	int a, t;
    cin >> a;
    //입력받은 횟수만큼 반복
    for(int i=1; i<=a; i++){
        t = i;
        bool check = true;
        //t가 0이될때까지 반복한다.
        //3으로 나누어떨어질시 -출력
    	while(t){
        if( t%10 && (t%10)%3 == 0){
            cout <<"-";
            check = false;
       	 	}
            t /= 10;
        }
        //위에서 한번도 걸리지 않았다면 숫자를 출력한다.
        if(check)   cout << i ;
        cout << " ";
    }
	return 0;
}