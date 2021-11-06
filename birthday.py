import numpy as np
nstd = 22
ntimes = 1000
fre = 0

for i in range(ntimes):
    s = 0
    data = np.random.uniform(1, 366, nstd)
    date = np.floor(data)
    date = np.array(date)
    newdate = set(date)
    nsize = len(newdate)
    if nsize < nstd:
        fre = fre+1

print(fre)
print(fre/ntimes)
