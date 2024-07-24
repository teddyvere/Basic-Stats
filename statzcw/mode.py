import pandas as pd

csvfile1 = pd.read_csv('dataOne.csv')
csvfile2 = pd.read_csv('dataTwo.csv')
csvfile3 = pd.read_csv('dataThree.csv')
csvfile0 = pd.read_csv('dataZero.csv')

def zmode(csv: pd.DataFrame) -> float :
    return csv.mode().iloc[0]

print(zmode(csvfile1))
print(zmode(csvfile2))
print(zmode(csvfile3))
print(zmode(csvfile0))