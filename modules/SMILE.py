import pandas as pd


def SMILEtoDataFrame(path):
    data = pd.read_csv(path, sep='\s+') # \s+ is the regex for whitespaces
    data.columns = ['SMILES', 'ID']
    return data

