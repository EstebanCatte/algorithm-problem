#include <iostream>
#define lli long long int
using namespace std;
const lli mod = 1e9 + 7;

//Iterative Function to calculate (x^y)%p in O(log y)
lli power(lli x, lli y, lli p)
{
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

int main()
{
    lli n;
    cin >> n;
    cout << power(2, n, mod);
    return 0;
}