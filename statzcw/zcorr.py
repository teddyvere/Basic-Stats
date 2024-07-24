import pandas as pd

csvfile1 = pd.read_csv('dataOne.csv')
csvfile2 = pd.read_csv('dataTwo.csv')
csvfile3 = pd.read_csv('dataThree.csv')
csvfile0 = pd.read_csv('dataZero.csv')

def zcorr(csv: pd.DataFrame) -> float :
    return csv.corr().iloc[0,1]

print(zcorr(csvfile1))
print(zcorr(csvfile2))
print(zcorr(csvfile3))
print(zcorr(csvfile0))