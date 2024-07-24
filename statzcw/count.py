import pandas as pd

csv_file = 'dataOne.csv'
csv_file2 = 'dataTwo.csv'
csv_file3 = 'dataThree.csv'
csv_file0 = 'dataZero.csv'

def count(csv_file: pd.DataFrame) -> float :
    return pd.read_csv(csv_file).count()

print(count(csv_file))
print(count(csv_file2))
print(count(csv_file3))
print(count(csv_file0))