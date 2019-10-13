import json
with open("gene_max_list.json", 'r') as file:
	data = json.load(file)
	f = open("geneset.txt", 'r')
	abc="ZBTB17"
	a=f.read()
	i=0
	gene_list=[]
	b=1
	start=0
	end=a.index("\n")
	lent=len(a)
	end2=a[end+2:].index("\n")
	while i!=2:
		gene_list.append(a[start:end])
		if i==1:
			break
		a=a[end+1:]
		try:
			end=a.index("\n")
		except:
			i=1
			end=697
	for i in data:
		for j in gene_list:
			if i==j:
				print(i)
	with open("gene_set_er.json", 'w') as fout:
		json.dump(gene_list, fout)