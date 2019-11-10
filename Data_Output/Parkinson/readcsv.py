import pandas as pd
#import xlrd
import json

hallmark_genes = ["ALDH18A1", "ARFGAP1", "ASNS", "ATF3", "ATF4", "ATF6", "ATP6V0D1", "BAG3", "BANF1", "CALR", "CCL2", "CEBPB", "CEBPG", "CHAC1", "CKS1B", "CNOT4", "CNOT6", "CXXC1", "DCP1A", "DCP2", "DCTN1", "DDIT4", "DDX10", "DKC1", "DNAJA4", "DNAJB9", "DNAJC3", "EDC4", "EDEM1", "EEF2", "EIF2AK3", "EIF2S1", "EIF4A1", "EIF4A2", "EIF4A3", "EIF4E", "EIF4EBP1", "EIF4G1", "ERN1", "ERO1A", "EXOC2", "EXOSC1", "EXOSC10", "EXOSC2", "EXOSC4", "EXOSC5", "EXOSC9", "FKBP14", "FUS", "GEMIN4", "GOSR2", "H2AFX", "HERPUD1", "HSP90B1", "HSPA5", "HSPA9", "HYOU1", "IARS", "IFIT1", "IGFBP1", "IMP3", "KDELR3", "KHSRP", "KIF5B", "LSM1", "LSM4", "MTHFD2", "MTREX", "NABP1", "NFYA", "NFYB", "NHP2", "NOLC1", "NOP14", "NOP56", "NPM1", "PAIP1", "PARN", "PDIA5", "PDIA6", "POP4", "PREB", "PSAT1", "RPS14", "RRP9", "SDAD1", "SEC11A", "SEC31A", "SERP1", "SHC1", "SLC1A4", "SLC30A5", "SLC7A5", "SPCS1", "SPCS3", "SRPRA", "SRPRB", "SSR1", "STC2", "TARS", "TATDN2", "TSPYL2", "TTC37", "TUBB2A", "VEGFA", "WFS1", "WIPI1", "XBP1", "XPOT", "YIF1A", "YWHAZ", "ZBTB17"]
pt = pd.read_csv('E-GEOD-72267-experiment-design.tsv', sep='\t')
df = pd.read_csv('E-GEOD-72267-A-AFFY-37-normalized-expressions.tsv', sep='\t')

patientsInSeq = {}
countet = 3
for cols in df.columns[3:]:
    patientsInSeq[cols] = countet
    countet+=1

print(patientsInSeq)

allPatients = {}
row_number=0
for i in pt.iloc[:,0]:
    print(i)
    #print(str(pt.iloc[row_number, 102]))
    if(str(pt.iloc[row_number, 2])=="normal"):
        allPatients[i] = 0
    else:
        allPatients[i] = 1
    row_number+=1

print(row_number)

patientdir = {}

tempdir={}
k=0
for i in df.iloc[:,1]:
    #print(i)
    if i in hallmark_genes:
        tempdir[i] = k
    k+=1

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



