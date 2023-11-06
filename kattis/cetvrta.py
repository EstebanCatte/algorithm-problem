def least_common(arr):
    return min(arr, key=arr.count)

x1,y1 = [int(i) for i in input().split()]
x2,y2 = [int(i) for i in input().split()]
x3,y3 = [int(i) for i in input().split()]

print(least_common([x1,x2,x3]), least_common([y1,y2,y3]))
