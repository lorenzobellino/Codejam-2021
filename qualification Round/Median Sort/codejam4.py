import numpy as np
ALPHABET = 'abcdefghijklmnopqrstuvwxyz'
T,N,Q = [int(x) for x in str(input()).split(" ")]

for t in range(T):
    answer = False
    n = {x:ALPHABET[x] for x in range(N)}
    resp =[]
    for i in range(1,len(n.keys())-1):
        print(i,i+1,i+2);
        l = int(input())
        if(i==l):
            a = np.array([i+1,i,i+2])
        elif(i+1 == l):
            a = np.array([i,i+1,i+2])
        elif(i+2==l):
            a = np.array([i,i+2,i+1])

        resp.append(a)
    k = np.stack((resp),axis=1)
    print(k)
