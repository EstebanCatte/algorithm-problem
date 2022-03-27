num_child = int(float(input()))
aj = [int(float(i)) for i in input().split()]

hapiness = 0
number = 0
for a in aj:
    #On suppose que le 0 est à la fin et on calcule
    if a == 0:
        continue
    number += 1
    hapiness += number*a 

res = hapiness
end = 0
for preference in reversed(aj):
    hapiness -= preference*number
    end += preference*(number+1)
    number -= 1
    total_sum = end + hapiness
    res = max(total_sum, res)

print(res)