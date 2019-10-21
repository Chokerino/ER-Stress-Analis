import heapq
import json
import operator
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import matplotlib.patches as mpatches

#print("fdsfdsf")			
#df = pd.read_csv('gene_expression.csv')
#print("fdsfdsf")			
#abc = sns.swarmplot(data=df)
#plt.xticks(rotation=90)
#plt.show()
df = pd.read_csv('gene_expression.csv')
#for region, df_region in df.groupby('stage'):
 #   sns.catplot(data=df_region)
  #  plt.xticks(rotation=90)
   # stage_name=region.replace(" ","_")
    #plt.title(region)
    #filename='gene_plots/expressed_genes_%s.png' %(stage_name)
    #plt.savefig(filename, dpi=1000, label="Expression")
    #plt.show()

plt.clf()
for stage, df_stage in df.groupby('stage'):
   for stage2, df_stage2 in df.groupby('stage'):
       if stage!=stage2:
            stage_name=stage.replace(" ","_")
            stage2_name=stage2.replace(" ","_")
            Green_patch = mpatches.Patch(color='green', label=stage2_name)
            Red_patch = mpatches.Patch(color='red', label=stage_name)
            sns.stripplot(data=df_stage,color="red",linewidth=0.7,marker="o",size=9)
            sns.stripplot(data=df_stage2,color="green",linewidth=0.5,marker="x",alpha=0.5,size=7)
            plt.xticks(rotation=70)
            plt.title(stage_name+" and "+stage2_name)
            filename='gene_plots/compare/expressed_genes_%s.png' %(stage_name+"+"+stage2_name)
            plt.legend(handles=[Red_patch,Green_patch])
            plt.savefig(filename, dpi=1000, label="Expression")
            plt.clf()

	