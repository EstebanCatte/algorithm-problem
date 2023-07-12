#include <iostream>
#define lli long long int
using namespace std;

int main()
{
    lli k;
    cin >> k;
    for (lli n = 1; n <= k; n++)
    {
        cout << n * n * (n * n - 1) / 2 - 4 * (n - 1) * (n - 2) << endl;
    }
    return 0;
}