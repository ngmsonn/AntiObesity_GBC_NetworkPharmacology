import os
import numpy as np
import pandas as pd


def filter(path, column_name):
    data = pd.read_csv(path)
    data_new = data[column_name]

    return data_new


def BuildData(data1, data2):
    
    list_data1 = np.array(data1).tolist()
    list_data2 = np.array(data2).tolist()
    for gene in list_data1:
        if gene not in list_data2:
            list_data2.append(gene)
    
    data_final = pd.DataFrame(list_data2)
    data_final.columns = ['Genes']

    return data_final

def RemoveDuplicates(data):
    if isinstance(data, pd.DataFrame):
        print("True")   
    else:
        data = pd.DataFrame(data)