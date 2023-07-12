#include <bits/stdc++.h>

using namespace std;

int n, x;

int main()
{  
    scanf("%d %d", &n, &x);
    int w[n];
    for(int i = 0; i < n; i++){
        scanf("%d", &w[i]);
    }

    sort(w, w+n);
    int aptr=0, bptr=n-1, res=0;
    for(int i =0; i<n ; i++){
        if(aptr == bptr)
        {
            res++;
            cout << res;
            return 0;
        }
        if(aptr > bptr){
            cout << res;
            return 0;
        }

        if(w[aptr] + w[bptr] <= x){
            aptr++;
            bptr--;
            res++;
        }
        else{
            bptr--;
            res++;
        }
    }
    return 0;
}