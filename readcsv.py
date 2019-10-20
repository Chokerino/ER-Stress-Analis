import pandas as pd
import xlrd
import json

hk = pd.read_csv('hallmark.csv')
pt = pd.read_csv('phtype.csv')
df = pd.read_csv('trycsv.csv')
hallmark_genes=[]
common_patients = []
for i in hk.iloc[:, 0]:
    hallmark_genes+=[i]

patientsInSeq = {}
countet = 0
for cols in df.columns:
    patientsInSeq[cols] = countet
    countet+=1

#print(patientsInSeq)

allPatients = {}
row_number=0
for i in pt.iloc[:,0]:
    if str(pt.iloc[row_number, 102])!="nan" and str(pt.iloc[row_number, 102])!="[Discrepancy]":
        allPatients[i] = str(pt.iloc[row_number, 102])
    row_number+=1

patientdir = {}

tempdir={}
k=0
for i in df.iloc[:,0]:
    #print(i)
    if i in hallmark_genes:
        tempdir[i] = k
    k+=1

# Pathological stage column = 102

patientDict = {}

for i in patientsInSeq:
    if i in allPatients.keys():
        if i not in patientDict.keys():
            patientDict[i]= []
            for genes in tempdir:
                temper={}
                yo = df.iloc[tempdir[genes],patientsInSeq[i]]
                temper[genes] = yo
                patientDict[i].append(temper)
            nono = {}
            patientDict[i].append(allPatients[i])


with open('patient_data_processed.json', 'w') as fout:
    json.dump(patientDict, fout)


#print(tempdir)



