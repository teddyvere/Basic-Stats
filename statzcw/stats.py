
from typing import List

def zcount(data: List[float]) -> float :
    return sum(1 for x in data if x > 0) / len(data)

def zmean(data: List[float]) -> float :
    return sum(data) / len(data)

def zmode(data: List[float]) -> float :
    return [num for num in data if data.count(num) == data.count(max(data))] 

def zmedian(data: List[float]) -> float :
    if len(data) % 2 == 0:
        mid = len(data) // 2
        return (data[mid] + data[mid - 1]) / 2
    else:
        return len(data) // 2
     

def zvariance(data: List[float]) -> float :
    mean = zmean(data)
    return sum((x - mean) ** 2 for x in data) / (len(data) - 1)
	
def zstddev(data: List[float]) -> float :
    # sqrt of variance
    var = zvariance(data)
    return var ** 0.5

def zstderr(data: List[float]) -> float :
    return zstddev(data) / zmean(data)

def cov(a, b):
    return cov(a, b) / (zstddev(a) * zstddev(b))

def zcorr(datax: List[float], datay: List[float]) -> float :
    return cov(datax, datay) * (zstddev(datax) / zstddev(datay))


def readDataFile(file):
    x,y = [], []
    with open(file) as f:
        first_line = f.readline() # consume headers
        for l in f:
            row = l.split(',')
            #print(row, type(row))
            x.append(float(row[0]))
            y.append(float(row[1]))
    return (x,y)

def readDataSets(files):
    data = {}
    for file in files:
        twoLists = readDataFile(file)
        data[file] = twoLists
    return data
