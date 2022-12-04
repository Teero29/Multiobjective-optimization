# Comparaison des solutions obtenus avec celles des autres étudiants / celles du prof

from utils import hypervolume, domine

file_name = "Data/solutions/LAP20-4obj.txt"

with open(file_name, 'r') as fin:
    scores = [tuple(map(int,line.strip().split())) for line in fin]

ref = (900,900,900,900)
h = hypervolume(ref, scores)
print(h)




