int t, temp, prev, total;

cin >> t;

for (int i = 0; i < t; i++) {
    total = 0;
    temp = 1;
    
    while (temp != 0) {
        prev = temp;
        cin >> temp;

        if (prev * 2 < temp) {
            total += temp - (prev * 2);
        }
    }

    cout << total << endl;

t = int(input(t))
for i in range(t):
    total = 0
    temp = 1
    while temp != 0:
        prev = temp
        temp = int(input())
        if (prev*2 < temp):
            total += temp - (prev *2)

    print(total)