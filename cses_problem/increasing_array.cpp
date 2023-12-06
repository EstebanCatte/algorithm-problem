#include <iostream>
#include <string>
#define lli long long int

using namespace std;

int main()
{
    lli n;
    cin >> n;
    lli arr[n];
    for (lli i = 0; i < n; i++){
        cin >> arr[i];
    }
    lli res=0, dp=arr[0];
    for (lli i = 0; i < n-1; i++){
        res += max(0ll, dp - arr[i+1]);
        dp = max(dp, arr[i+1]);
    }
    cout << res;
    return 0;
}







