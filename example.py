import numpy as np
import tricubic

n = 3
f = np.zeros((n,n,n), dtype='float')

for i in range(n):
  for j in range(n):
    for k in range(n):
      f[i][j][k] = i+j+k #some function f(x,y,z) is given on a cubic grid indexed by i,j,k
      
ip = tricubic.tricubic(list(f), [n,n,n]) #initialize interpolator with input data on cubic grid
for i in range(100000):
  res = ip.ip(list(np.random.rand(3)*(n-1))) #interpolate the function f at a random point in space
  #print res
