#include <bits/stdc++.h>
using namespace std;

void hanoi(int from, int to, int depth){
    if(depth == 1){
        cout << from << " " << to << endl;
        return;
    }

    int other = 6 - from - to;
    hanoi(from, other, depth-1);
    cout << from << " " << to << endl;
    hanoi(other, to, depth-1);
}

int main()
{
    int n;
    cin >> n;
    cout << pow(2, n)-1 << endl;
    hanoi(1, 3, n);
    return 0;
}