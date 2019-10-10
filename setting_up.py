import pandas as pd
import matplotlib.pyplot as plt 
import heapq
#df = pd.read_excel (r'HiSeqV2.xlsx') #for an earlier version of Excel, you may need to use the file extension of 'xls'
import json
#print (df)
import xlrd 
book = xlrd.open_workbook('HiSeqV2.xlsx')
sheet=[]
max_list=[]
min_list=[]
common=[]
genes_max_dict={}
genes_min_dict={}
gene_max_expression={}
gene_min_expression={}
pos=0
for x in book.sheets():
	sheet.append(x)
for i in range(1,sheet[0].ncols):
	max_gene=[]
	min_gene=[]
	max_list=heapq.nlargest(20,sheet[0].col_values(i)[1:])
	min_list=heapq.nsmallest(20,sheet[0].col_values(i)[1:])
	for j in max_list:
		pos=sheet[0].col_values(i)[1:].index(j)
		gene_name=sheet[0].col_values(0)[1:][pos]
		max_gene.append(sheet[0].col_values(0)[1:][pos])
		if gene_name not in gene_max_expression:
			gene_max_expression[gene_name]=sheet[0].col_values(i)[1:].index(j)
		else:
			gene_max_expression[gene_name]+=sheet[0].col_values(i)[1:].index(j)

	for j in min_list:
		pos=sheet[0].col_values(i)[1:].index(j)
		gene_name=sheet[0].col_values(0)[1:][pos]
		min_gene.append(gene_name)
		if gene_name not in gene_min_expression:
			gene_min_expression[gene_name]=sheet[0].col_values(i)[1:].index(j)
		else:
			gene_min_expression[gene_name]+=sheet[0].col_values(i)[1:].index(j)	

	for g in max_gene:
		if g not in genes_max_dict:
			genes_max_dict[g]=1
		else:
			genes_max_dict[g]+=1
	for g in min_gene:
		if g not in genes_min_dict:
			genes_min_dict[g]=1
		else:
			genes_min_dict[g]+=1				

	plt.plot(max_gene,max_list,label=sheet[0].col_values(i)[0])
	#print(sheet[0].col_values(i))
   
with open('gene_max_list.json', 'w') as fout:
    json.dump(genes_max_dict, fout)
with open('gene_min_list.json', 'w') as fout:
    json.dump(genes_min_dict , fout)
with open('gene_min_expression.json', 'w') as fout:
    json.dump(gene_min_expression , fout)
with open('gene_max_expression.json', 'w') as fout:
    json.dump(gene_max_expression , fout)            
plt.savefig('gene_to_patient.png', dpi=1000)
plt.show()
plt.close()
