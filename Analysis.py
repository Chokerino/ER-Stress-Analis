import heapq
import json
import operator
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size': 8}) 
with open("gene_max_list.json", 'r') as file:
	data = json.load(file)
	max_genes=dict(sorted(data.items(), key=operator.itemgetter(1), reverse=True)[:10])
	print(max_genes)
	gene_name=[]
	gene_number=[]
	fig, (ax1, ax2) = plt.subplots(2)
	ax1.set_title('Maximum Expressed Genes')
	ax2.set_title('Maximum Expression Value')
	for i in max_genes:
		gene_name.append(i)
		gene_number.append(max_genes[i])
	ax1.plot(gene_name,gene_number)
	plt.xlabel('Gene Name')
	ax1.set_ylabel('Number of Patients')
	ax2.set_ylabel('Expresssion Value')
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
		plt.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=None, hspace=0.5)
		plt.show()


with open("gene_min_list.json", 'r') as file:
	data = json.load(file)
	max_genes=dict(sorted(data.items(), key=operator.itemgetter(1), reverse=True)[:10])
	print(max_genes)
	gene_name=[]
	gene_number=[]
	plt.rcParams.update({'font.size': 8}) 
	fig, (ax1, ax2) = plt.subplots(2)
	ax1.set_title('Minimum Expressed Genes')
	ax2.set_title('Minimum Expression Value')
	for i in max_genes:
		gene_name.append(i)
		gene_number.append(max_genes[i])
	ax1.plot(gene_name,gene_number)
	plt.xlabel('Gene Name')
	ax1.set_ylabel('Number of Patients')
	ax2.set_ylabel('Expresssion Value')
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
		plt.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=None, hspace=0.5)
		plt.show()

with open("patient_data_withgenesAnd_stages.json", 'r') as file:
	data = json.load(file)
	lbel=""
	q=[]
	stages=[]
	max_occu={}
	for i in data:
		z={}
		for j in data[i]:
			for k in j:
				if(isinstance(j,dict)):
						z[k]=j[k]
				else:
					lbel=j
					if j not in stages:
						stages.append(j)
		x=[]
		y=[]			
		sorted_x=dict(sorted(z.items(), key=operator.itemgetter(1), reverse=True)[:5])
		for i in sorted_x:
			if i not in max_occu:
				max_occu[i]=1
			else:
				max_occu[i]+=1	
		for i in sorted_x:
			x.append(i)
			y.append(sorted_x[i])
			if i not in q:
				q.append(i)

		plt.plot(x,y, label=lbel)
	plt.show()
	print(stages)
	max_occu=dict(sorted(max_occu.items(), key=operator.itemgetter(1), reverse=True))
	with open('er_gene_max_occurence.json', 'w') as fout:
		json.dump(max_occu , fout)
	#print(max_occu)						