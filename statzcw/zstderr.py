import pandas as pd

csvfile1 = pd.read_csv('dataOne.csv')
csvfile2 = pd.read_csv('dataTwo.csv')
csvfile3 = pd.read_csv('dataThree.csv')
csvfile0 = pd.read_csv('dataZero.csv')

def zsetderr(csv: pd.DataFrame) -> float :
    return csv.std()

print(zsetderr(csvfile1))
print(zsetderr(csvfile2))
print(zsetderr(csvfile3))
print(zsetderr(csvfile0))
