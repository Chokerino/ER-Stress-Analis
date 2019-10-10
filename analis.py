import heapq
import json
import operator
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size': 9}) 
with open("gene_max_list.json", 'r') as file:
	data = json.load(file)
	max_genes=dict(sorted(data.items(), key=operator.itemgetter(1), reverse=True)[:10])
	print(max_genes)
	gene_name=[]
	gene_number=[]
	fig, (ax1, ax2) = plt.subplots(2)
	fig.suptitle('Max Expressed Genes and Max Expression Value')
	for i in max_genes:
		gene_name.append(i)
		gene_number.append(max_genes[i])
	ax1.plot(gene_name,gene_number)
	with open("gene_max_expression.json", 'r') as file1:
		data1 = json.load(file1)
		max_genes=dict(sorted(data1.items(), key=operator.itemgetter(1), reverse=True)[:10])
		print(max_genes)
		gene_name=[]
		gene_number=[]
		for i in max_genes:
			gene_name.append(i)
			gene_number.append(max_genes[i])
		ax2.plot(gene_name,gene_number)
		plt.savefig('most_expressed_genes.png', dpi=1000, label="Expression")
		plt.show()

with open("gene_min_list.json", 'r') as file:
	data = json.load(file)
	max_genes=dict(sorted(data.items(), key=operator.itemgetter(1), reverse=True)[:10])
	print(max_genes)
	gene_name=[]
	gene_number=[]
	plt.rcParams.update({'font.size': 8}) 
	fig, (ax1, ax2) = plt.subplots(2)
	fig.suptitle('Min Expressed Genes and Min Expression Value')
	for i in max_genes:
		gene_name.append(i)
		gene_number.append(max_genes[i])
	ax1.plot(gene_name,gene_number)
	with open("gene_min_expression.json", 'r') as file:
		data = json.load(file)
		max_genes=dict(sorted(data.items(), key=operator.itemgetter(1), reverse=True)[:10])
		print(max_genes)
		gene_name=[]
		gene_number=[]
		for i in max_genes:
			gene_name.append(i)
			gene_number.append(max_genes[i])
		ax2.plot(gene_name,gene_number)
		plt.savefig('least_expressed_genes.png', dpi=1000, label="Expression")
		plt.show()	