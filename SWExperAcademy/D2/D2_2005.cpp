#include <iostream>
#include <string>

using namespace std;
// D2_2005 파스칼 삼각형

int main(){
    int length, a;
    cin >> length;
    for(int k=1; k<= length; k++){
        cin >> a;
        //삼각형의 크기는 10이하이므로 10X10의 배열로 잡는다.
		int pa[10][10];
        //제일왼쪽열과 제일위쪽행을 1로 초기화합니다.
    	for (int i = 0; i < a; i++){
			pa[0][i] = 0;
        	pa[i][0] = 1;
		}
        //반복을 돌면서자신의 위쪽과 왼쪽위를 더하며 계산해 나간다.
    	for(int i=1; i<a; i++){
    		for(int j=1; j<a; j++){
        		pa[i][j] = pa[i-1][j-1] + pa[i-1][j];
        	}
    	}
        //출력
        cout << "#"<<k<<endl;
    	for(int i=0; i<a; i++){
    		for(int j=0; j<=i; j++){
        		cout << pa[i][j] << " ";
        	}
        	cout<<endl;
    	}
    }
	return 0;
}