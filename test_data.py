import heapq
import json
import operator
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df = pd.read_csv('gene_expression.csv')
for region, df_region in df.groupby('stage'):
    for region2, df_region2 in df.groupby('stage'):
        print(region, region2)
	