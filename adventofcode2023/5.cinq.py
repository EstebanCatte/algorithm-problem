import re
with open("./input5.txt") as f:
    ls = f.read().strip().split("\n")
      
seeds = [int(n.group()) for n in re.finditer(r'\d+', ls[0])]

seed_to_soil = []
for i in range(3,35):
    nums = [int(a) for a in ls[i].split(' ')]
    seed_to_soil.append({"dest":nums[0], "source":nums[1], "len":nums[2]})


soil_to_fert = []
for i in range(37,72):
    nums = [int(a) for a in ls[i].split(' ')]
    soil_to_fert.append({"dest":nums[0], "source":nums[1], "len":nums[2]})
   
    
fert_to_water = []
for i in range(74,101):
    nums = [int(a) for a in ls[i].split(' ')]
    fert_to_water.append({"dest":nums[0], "source":nums[1], "len":nums[2]})
    
    
water_to_light = []
for i in range(103,120):
    nums = [int(a) for a in ls[i].split(' ')]
    water_to_light.append({"dest":nums[0], "source":nums[1], "len":nums[2]})
    
    
light_to_temp = []
for i in range(122,164):
    nums = [int(a) for a in ls[i].split(' ')]
    light_to_temp.append({"dest":nums[0], "source":nums[1], "len":nums[2]})
    

temp_to_hum = []
for i in range(166,203):
    nums = [int(a) for a in ls[i].split(' ')]
    temp_to_hum.append({"dest":nums[0], "source":nums[1], "len":nums[2]})
    
 
hum_to_loc = []
for i in range(205,236):
    nums = [int(a) for a in ls[i].split(' ')]
    hum_to_loc.append({"dest":nums[0], "source":nums[1], "len":nums[2]})
    
  
#===============================PART 1==========================
def find(seed, dict_list):
    for dic in dict_list:
        if seed >= dic["source"] and seed <= dic["source"]+dic["len"]:
            return dic["dest"]+seed-dic["source"]
    return seed

dict_list = [seed_to_soil, soil_to_fert, fert_to_water, water_to_light, light_to_temp, temp_to_hum, hum_to_loc]
res = 1e30
for i in range(0,20,2):
    for seed in seeds:
        variable = seed
        for d in dict_list:
            variable = find(variable, d)
        res = min(res, variable)
    
print(res)
    
#===============================PART 2========================== 
#Par le bas, on part des locations et on remonte petit à petit  
def find(dic, dic_list):
    new_intervals = []
    for sup in dic_list:
        
        borneA = dic["source"]+dic["len"] - sup["dest"]
        borneB = sup["dest"]+sup["dest"] - dic["source"]
        if borneA <= 0 and dic["source"] <= sup["dest"]:
            continue
        if borneB <= 0 and sup["dest"] <= dic["source"]:
            continue
        interv = [max(dic["source"], sup["dest"]), min(dic["source"]+dic["len"], sup["dest"]+sup["dest"])]
        new_intervals.append({"dest":interv[0], "source"})
        print("new interv = {}".format(new_intervals))
        
res = 1e30
for l in hum_to_loc:
    find(l, temp_to_hum)


##NEED TO PROCESS INTERVALS
    
    