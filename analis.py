import heapq
import json
import operator
import matplotlib.pyplot as plt 
with open("gene_max_list.json", 'r') as file:
	data = json.load(file)
	max_genes=dict(sorted(data.items(), key=operator.itemgetter(1), reverse=True)[:10])
	print(max_genes)
	gene_name=[]
	gene_number=[]
	for i in max_genes:
		gene_name.append(i)
		gene_number.append(max_genes[i])
	plt.plot(gene_name,gene_number)
	plt.savefig('most_occuring_max_genes.png', dpi=1000)
	plt.show()

with open("gene_min_list.json", 'r') as file:
	data = json.load(file)
	max_genes=dict(sorted(data.items(), key=operator.itemgetter(1), reverse=True)[:10])
	print(max_genes)
	gene_name=[]
	gene_number=[]
	for i in max_genes:
		gene_name.append(i)
		gene_number.append(max_genes[i])
	plt.plot(gene_name,gene_number)
	plt.savefig('least_occuring_min_genes.png', dpi=1000)
	plt.show()

			
with open("gene_max_expression.json", 'r') as file:
	data = json.load(file)
	max_genes=dict(sorted(data.items(), key=operator.itemgetter(1), reverse=True)[:10])
	print(max_genes)
	gene_name=[]
	gene_number=[]
	for i in max_genes:
		gene_name.append(i)
		gene_number.append(max_genes[i])
	plt.plot(gene_name,gene_number)
	plt.savefig('most_expressed_min_genes.png', dpi=1000)
	plt.show()

with open("gene_min_expression.json", 'r') as file:
	data = json.load(file)
	max_genes=dict(sorted(data.items(), key=operator.itemgetter(1), reverse=True)[:10])
	print(max_genes)
	gene_name=[]
	gene_number=[]
	for i in max_genes:
		gene_name.append(i)
		gene_number.append(max_genes[i])
	plt.plot(gene_name,gene_number)
	plt.savefig('least_expressed_min_genes.png', dpi=1000)
	plt.show()	