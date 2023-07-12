#include <iostream>
#define lli long long int
using namespace std;

int main()
{
    lli test, x, y, r;
    cin >> test;
    lli res[test];
    for (int i = 0; i < test; i++){
        cin >> y;
        cin >> x;
        if(x >= y){
            if(x%2 == 1){
                r = x*x - y + 1 ;
            }else{
                r = (x-1)*(x-1) + y ;
            }
        }else{
            if(y%2 == 0){
                r = y*y - x +1;
            }else{
                r = (y-1)*(y-1) + x ;
            }
        }
        res[i] = r;
    }
    for (int i = 0; i < test; i++){
        cout << res[i] << endl;
    }
    return 0;
}





