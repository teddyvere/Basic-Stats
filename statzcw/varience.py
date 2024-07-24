import pandas as pd

csvfile1 = pd.read_csv('dataOne.csv')
csvfile2 = pd.read_csv('dataTwo.csv')
csvfile3 = pd.read_csv('dataThree.csv')
csvfile0 = pd.read_csv('dataZero.csv')

def zvariance(data1: pd.DataFrame) -> float :
    return data1.var()

print(zvariance(csvfile1))
print(zvariance(csvfile2))
print(zvariance(csvfile3))
print(zvariance(csvfile0))