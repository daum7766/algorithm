//D3 9317 석찬이의 받아쓰기
#include <iostream>
#include <string>

using namespace std;

int main(){
    int length;
    cin >> length;
    for(int t=1; t<=length; t++){
        int n, count = 0;
        string a, b ;
        cin >> n;
        cin >> a >> b;
        for(int i=0; i<n; i++){
        	if(a[i] == b[i])count++;
        }
    	cout << "#" << t << " " << count <<endl;
    }
	return 0;
}