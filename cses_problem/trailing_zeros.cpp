#include <iostream>
using namespace std;

//The idea is to consider prime factors of a factorial n. 
//A trailing zero is always produced by prime factors 2 and 5. 
//If we can count the number of 5s and 2s, our task is done

int main()
{
    int n;
    cin >> n;
    int total = 0;
    for (int i = 5; n / i >= 1; i *= 5)
    {
        total += n / i;
    }
    cout << total;
    return 0;
}