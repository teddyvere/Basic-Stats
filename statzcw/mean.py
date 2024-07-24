import pandas as pd

csvfile1 = pd.read_csv('dataOne.csv')
csvfile2 = pd.read_csv('dataTwo.csv')
csvfile3 = pd.read_csv('dataThree.csv')
csvfile0 = pd.read_csv('dataZero.csv')

def zmean(csv: pd.DataFrame) -> float :
    return csv.mean()

print(zmean(csvfile1))
print(zmean(csvfile2))
print(zmean(csvfile3))
print(zmean(csvfile0))