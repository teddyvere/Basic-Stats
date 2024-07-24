import pandas as pd

csvfile1 = pd.read_csv('dataOne.csv')
csvfile2 = pd.read_csv('dataTwo.csv')
csvfile3 = pd.read_csv('dataThree.csv')
csvfile0 = pd.read_csv('dataZero.csv')

def zmedian(csv: pd.DataFrame) -> float :
   return csv.median()
    
print(zmedian(csvfile1))
print(zmedian(csvfile2))
print(zmedian(csvfile3))
print(zmedian(csvfile0))