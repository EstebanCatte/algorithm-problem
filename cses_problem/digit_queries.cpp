#include <bits/stdc++.h>

using namespace std;
typedef long long ll;

ll pow10(int x){
    ll res = 1;
    for(int i = 0; i < x; i++)
        res *= 10;
    return res;
}

int solve(ll N){
    if(N < 9)
    {
        return (int) N+1;
    }
    int len = 1;
    //parcours les nombres de differentes taille. Il y a 9*10^len nombre a chaque len
    while(9 * pow10(len-1) * len < N){
        N -= 9 * pow10(len-1) * len;
        len++;
    }

    string S = to_string(pow10(len-1) + N/len);
    return (int) (S[N%len] - '0');
}

int main(){
    int num;
    ll in;
    cin >> num;
    for(int q = 0; q < num; q++){
        cin >> in;
        cout << solve(in-1) << endl;
    }
}