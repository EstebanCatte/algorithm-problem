R, C, Zr, Zc = [int(x) for x in input().split()]
m = []
for _ in range(R * Zr):
    m.append(["*"] * C * Zc)

for row in range(R):
    for col, char in enumerate(input()):
        r_offset = row*Zr
        c_offset = col*Zc
        for rv in range(r_offset, r_offset+Zr):
            for rc in range(c_offset, c_offset+Zc):
                m[rv][rc]=char

for row in m:
    print(''.join(row))
    