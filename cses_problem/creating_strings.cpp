#include <bits/stdc++.h>
#include <iostream>
#include <set>
#include <string>

using namespace std;

int N;
char S[9];
set<string> perms;

int main(){
    scanf("%s", S);
    N = (int) strlen(S);
    sort(S, S+N);

    perms.insert(S);
    while(next_permutation(S, S+N)){
        perms.insert(string(S, S+N));
    }

    cout << perms.size() << '\n';
    set<string>::iterator it;
    for( it = perms.begin(); it != perms.end(); ++it) {
        cout << *it << endl;
    }
        
    
}