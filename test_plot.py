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
for region, df_region in df.groupby('stage'):
    plt.figure(figsize=(14,13))
    sns.stripplot(data=df_region,size=15,marker="o",color="red",linewidth=0.5)
    plt.xticks(rotation=90)
    stage_name=region.replace(" ","_")
    plt.title(region)
    filename='gene_plots/expressed_genes_%s.png' %(stage_name)
    plt.grid(axis="x")
    plt.savefig(filename)
    plt.close()


for stage, df_stage in df.groupby('stage'):
   for stage2, df_stage2 in df.groupby('stage'):
    plt.figure(figsize=(14,13))
    if stage!=stage2:
        stage_name=stage.replace(" ","_")
        stage2_name=stage2.replace(" ","_")
        Green_patch = mpatches.Patch(color='green', label=stage2_name)
        Red_patch = mpatches.Patch(color='red', label=stage_name)
        sns.stripplot(data=df_stage,color="red",linewidth=0.7,marker="o",size=9)
        sns.stripplot(data=df_stage2,color="green",linewidth=0.5,marker="x",alpha=0.5,size=7)
        plt.xticks(rotation=90,fontsize=7)
        plt.title(stage_name+" and "+stage2_name)
        filename='gene_plots/compare/expressed_genes_%s.png' %(stage_name+"+"+stage2_name)
        plt.legend(handles=[Red_patch,Green_patch])
        plt.grid(axis="x")
        plt.savefig(filename)
        plt.close()

for stage, df_stage in df.groupby('stage'):
    for stage2, df_stage2 in df.groupby('stage'):
        if stage!=stage2:
            plt.figure(figsize=(14,13))
            stage_name=stage.replace(" ","_")
            stage2_name=stage2.replace(" ","_")
            Green_patch = mpatches.Patch(color='black', label=(stage2_name+" Mean"))
            Red_patch = mpatches.Patch(color='blue', label=(stage_name+" Mean"))  
            for i in df_stage.head():
                if i != "Patient Name" and i!="stage":
                    plt.scatter(i,df_stage[i].mean(),marker="o",color="black",s=15)
            for i in df_stage2.head():
                if i != "Patient Name" and i!="stage":    
                    plt.scatter(i,df_stage2[i].mean(),marker="^",color="blue",s=15)
            filename='gene_plots/mean/expressed_genes_%s.png' %(stage_name+"+"+stage2_name+"_Mean")
            plt.legend(handles=[Red_patch,Green_patch])
            plt.xticks(rotation=90,fontsize=7)
            plt.grid()
            plt.savefig(filename)        
            plt.close()
            