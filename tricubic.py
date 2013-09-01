import numpy as np
import tricubic

n = 3
xyz = np.zeros((n,n,n), dtype='float')

for i in range(n):
  for j in range(n):
    for k in range(n):
      xyz[i][j][k] = i+j+k
      
ip = tricubic.tricubic(list(xyz), [n,n,n])
for i in range(100000):
  res = ip.ip(list(np.random.rand(3)))
  #print res