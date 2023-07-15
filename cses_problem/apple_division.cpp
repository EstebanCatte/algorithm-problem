#include <bits/stdc++.h>
#define lli long long int
using namespace std;
 
int main()
{
	lli n, total=0, ans=INT_MAX;
	cin >> n;
	lli arr[n];
    //tale input
	for(lli i = 0; i < n; i++) {
		cin >> arr[i];
		total += arr[i];
	}

    //checking all solutions
	for(lli i = 0; i < 1<<n; i++) {
		lli s = 0;
		for(lli j = 0; j < n; j++) {
			if(i & 1<<j){
                s += arr[j];
            } 
		}
		lli curr = abs((total-s)-s);
		ans = min(ans, curr);
	}
	cout << ans;
	return 0;
}