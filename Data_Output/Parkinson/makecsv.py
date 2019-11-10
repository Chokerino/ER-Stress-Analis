import pandas
import json
import csv

mydict = []
with open('patient_data_processed.json') as p:
    jsfile = json.load(p)
    for i in jsfile:
        tmp = {}
        print(type(jsfile[i]))
        for j in range(0,len(jsfile[i])-1):
            for s in jsfile[i][j]:
                tmp[s] = jsfile[i][j][s]
        tmp['Patient'] = i
        tmp['Status'] = jsfile[i][-1]
        mydict.append(tmp)

fields = []
fields.append('Patient')

with open('patient_data_processed.json') as fl:
    jfile = json.load(fl)
    dc = jfile["GSM1859090"]
    for i in range(0, len(dc)-1):
        for j in dc[i]:
            fields.append(j)


fields.append('Status')

filename = "parkinsons.csv"

with open(filename, 'w') as csvfile: 
    writer = csv.DictWriter(csvfile, fieldnames = fields) 
      
    writer.writeheader() 
      
    writer.writerows(mydict)
