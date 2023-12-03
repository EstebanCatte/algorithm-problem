import re

def extract_numbers_from_line(line):
    return [int(num) for num in re.findall(r'\d+', line)]

file_path = "C:/Users/Esteban/Documents/GitHub/algorithm-problem/adventofcode2023/input2.txt"  # Remplacez par le chemin de votre fichier
lin = []
with open(file_path, 'r') as file:
    lines = file.readlines()
    for l in lines:
        lin.append(l.split())