#include <bits/stdc++.h>
using namespace std;


int main()
{  
    int N, x;
    set<int> s;
    scanf("%d", &N);
    for(int i=0; i<N; i++){
        scanf("%d", &x);
        s.insert(x);
    }
    printf("%d\n", (int) s.size());
    return 0;
}