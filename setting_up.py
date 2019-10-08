import pandas as pd
import matplotlib.pyplot as plt 
import heapq
#df = pd.read_excel (r'HiSeqV2.xlsx') #for an earlier version of Excel, you may need to use the file extension of 'xls'
#print (df)
import xlrd 
book = xlrd.open_workbook('HiSeqV2.xlsx')
sheet=[]
max_list=[]
common=[]
genes={}
print(type(book.sheets()))
for x in book.sheets():
	sheet.append(x)
for i in range(1,sheet[0].ncols):
	max_gene=[]
	max_list_positions=[]
	max_list=heapq.nlargest(20,sheet[0].col_values(i)[1:])
	for j in max_list:
		max_list_positions.append(sheet[0].col_values(i)[1:].index(j))
	for j in max_list_positions:
		max_gene.append(sheet[0].col_values(0)[1:][j])
	for g in max_gene:
		if g not in genes:
			genes[g]=1
		else:
			genes[g]+=1		
	plt.plot(max_gene,max_list,label=sheet[0].col_values(i)[0])
	#print(sheet[0].col_values(i))
   
print(genes)
import json
with open('gene_max_list.json', 'w') as fout:
    json.dump(genes, fout)    
plt.savefig('gene_to_patient.png', dpi=1000)
plt.show()
plt.close()
