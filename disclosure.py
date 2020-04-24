import pandas as pd
import numpy as np
from scipy.spatial import distance
import pandas as pd
import math
from sklearn import preprocessing
    
def main():
    originalx = pd.read_excel("/Users/mark_nicoli/Downloads/CASCrefmicrodata.xls")  
    mean = 0
    standDev = 1
    normalized_df = (originalx-originalx.min())/(originalx.max()-originalx.min())
    noise = np.random.normal(mean, standDev, [1080,13]) 
    signal = normalized_df + noise
    print(dbrl(normalized_df, signal))

def edistance(record1, record2): 
    return math.sqrt(sum((record1-record2)*(record1-record2)))

def dbrl(original, masked):
    original = original.to_numpy()
    masked = masked.to_numpy()

    i = 1
    reindentified = 0
    while i < len(original):
        j = 1
        minDist = 100000
        minRecord = -1
        while j < len(masked):
            if edistance(original[i,], masked[j,]) < minDist:
                minDist = edistance(original[i,], masked[j,])
                minRecord = j
            j += 1
        if minRecord == i:
            reindentified += 1
        i += 1
    return reindentified / 1080 * 100, np.square(np.subtract(original, masked)).mean()

if __name__ == '__main__':
    main()