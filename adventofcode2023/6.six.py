# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 08:32:40 2023

@author: EC266662
"""

import math

def travel(speed, time_left):
    return speed*time_left

def one(time, distance_max):
    number = 0
    for i in range(time+1):
        distance = travel(i,time-i)
        print("distance = {}".format(distance))
        if distance > distance_max:
            print("Valid, adding {}".format(i))
            number += 1
    return number


def two(time, distance):
    b1 = math.floor((time + math.sqrt(pow(time, 2) - 4 * distance))/2)
    b2 = math.ceil((time - math.sqrt(pow(time, 2) - 4 * distance))/2)

    return b1 - b2 + 1

times = [48876981]
distances = [255128811171623]
res = 1
#for i in range(len(times)):
    #res *= one(times[i], distances[i])

print(two(times[0], distances[0]))







