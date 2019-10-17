import json
import csv

set1 = set()

fields = ['PatientName']

with open("patient_data_withgenesAnd_stages.json") as file:
    f = json.load(file)
    for i in f:
        for x in range(0, len(f[i])-1):
            for s in f[i][x]:
                set1.add(s)

len(set1)

for i in set1:
    fields.append(i)

print(fields)