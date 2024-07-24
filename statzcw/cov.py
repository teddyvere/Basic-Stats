import pandas as pd

csvfile1 = pd.read_csv('dataOne.csv')
csvfile2 = pd.read_csv('dataTwo.csv')
csvfile3 = pd.read_csv('dataThree.csv')
csvfile0 = pd.read_csv('dataZero.csv')

def cov(data1: pd.DataFrame)-> float :
    return data1.cov().iloc[0,1]

print(cov(csvfile1))
print(cov(csvfile2))
print(cov(csvfile3))
print(cov(csvfile0))