#include <iostream>
#include <vector>
#define lli long long int
#define li long int
using namespace std;

int main()
{
    lli n;
    cin >> n;
    lli total = n * (n + 1) / 2;
    if (total & 1)
    {
        cout << "NO";
    }
    else
    {
        cout << "YES" << endl;
        vector<lli> arr1, arr2;
        total /= 2LL;
        while (n)
        {
            if (total - n >= 0)
            {
                arr1.push_back(n);
                total -= n;
            }
            else
            {
                arr2.push_back(n);
            }
            n--;
        }
        cout << arr1.size() << endl;
        for (lli i=0; i<arr1.size();i++)
            cout << arr1[i] << " ";
        cout << endl;
        cout << arr2.size() << endl;
        for (lli i=0; i<arr2.size();i++)
            cout << arr2[i] << " ";
    }
    return 0;
}