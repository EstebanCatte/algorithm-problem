#include <iostream>
#define lli long long int
using namespace std;

//Iterative Function to calculate (x^y)%p in O(log y)
lli power(lli x, lli y, lli p)
{   
    lli mod = 1e9 + 7;
    // (x^y) mod p
    lli res = 1;
    x %= p;
    while (y)
    {
        if (y & 1)
            res = (res * x) % p;
        y >>= 1;
        x = (x * x) % p;
    }
    return res;
}


//calculating the hash of a string s, which contains only lowercase letters
//p is 31 because its the nearest prime number near 26 lowercase letters; (53 for lower and upper)
long long compute_hash(string const& s) {
    const int p = 31;
    const int m = 1e9 + 9;
    long long hash_value = 0;
    long long p_pow = 1;
    for (char c : s) {
        hash_value = (hash_value + (c - 'a' + 1) * p_pow) % m;
        p_pow = (p_pow * p) % m;
    }
    return hash_value;
}

//Compute factorial
int factorial(int n){
    return (n == 1 || n == 0) ? 1 : factorial(n - 1) * n
}



//Go across all permutations of a string S of length N
while(next_permutation(S, S+N)){
        //do;
    }

//compute power of 10
ll pow10(int x)
{
    ll res = 1;
    for(int i = 0; i < x; i++)
        res *= 10;
    return res;
}

