def riempiSx(v,jmp,start,end,firstN):
    if(len(jmp)==0):
        while(start>=end and v[start]==0):
            v[start]=firstN
            firstN+=1
            start-=1
        return
    x = jmp[0]
    jmp = jmp[1:]
    k=start
    for k in range(start,end+x,-1):
        v[k] = firstN
        firstN+=1
    v[end] = firstN
    riempiDx(v,jmp,end+1,start,firstN+1)

def riempiDx(v,jmp,start,end,firstN):
    if(len(jmp)==0):
        while(start<=end and v[start]==0):
            v[start]=firstN
            firstN+=1
            start+=1
        return
    x = jmp[0]
    jmp = jmp[1:]
    k=start
    for k in range(start,end-x):
        v[k] = firstN
        firstN+=1
    v[end]=firstN
    riempiSx(v,jmp,end-1,k,firstN+1)


def solve():
    maxScore = int((N-1)*(N+2)/2)
    if(C<N-1):
        print('Case #'+str(i+1)+': IMPOSSIBLE')
        return
    if(C>maxScore):
        print('Case #'+str(i+1)+': IMPOSSIBLE')
        return

    tot = C-(N-1)
    jmp = []
    v = [0 for x in range(N)]
    for j in range(N-1,0,-1):
        if(tot-j>=0):
            jmp.append(j)
            tot-=j
    riempiDx(v,jmp,0,len(v)-1,1)
    print("Case #"+str(i+1)+": ",end='')
    for y in v:
        print(str(y)+" ",end='')
    print('')

T = int(input())
N=0
C=0
for i in range(T):
    N,C = [int(x) for x in input().split(' ')]
    solve()
