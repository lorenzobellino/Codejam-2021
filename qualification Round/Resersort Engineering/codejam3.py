
def riempiSx(v,jmp,start,end,firstN):
    # print('SX')
    # print(v)
    v[end]=firstN
    firstN+=1
    end-=1
    # print(v)
    print(start)
    print(end)
    if(len(jmp)==0):
        for z in range(end,start-1,-1):
            v[z]=firstN
            firstN+=1
        return
    x = jmp[0]
    jmp = jmp[1:]
    z=end
    for z in range(end,start+x,-1):
        # print(z)
        v[z]=firstN
        firstN+=1
        # print("\t"+str(v))
    print(v)
    riempiDx(v,jmp,start,z-x+1,firstN)

def riempiDx(v,jmp,start,end,firstN):
    # print("DX")
    # print(v)
    v[start]=firstN
    firstN+=1
    start+=1
    # print(v)
    # print(start)
    # print(end)
    if(len(jmp)==0):
        for k in range(start-1,end+1):
            v[k]=firstN
            firstN+=1
        return
    x = jmp[0]
    jmp = jmp[1:]
    k=start
    print(start)
    print(end)
    for k in range(start-1,end-x+1):
        v[k]=firstN
        firstN+=1
        # print("\t"+str(v))
    print(v)
    print(k)
    riempiSx(v,jmp,k,start+x-1,firstN)

T = int(input())
for i in range(T):
    N,C = [int(x) for x in input().split(' ')]
    maxScore = int((N-1)*(N+2)/2)
    if(C<N-1):
        print('Case #'+str(i+1)+': IMPOSSIBLE')
    elif(C>maxScore):
        print('Case #'+str(i+1)+': IMPOSSIBLE')
    else:
        tot = C-(N-1)
        jmp = []
        v = [0 for x in range(N)]
        for j in range(N-1,0,-1):
            if(tot-j>=0):
                jmp.append(j)
                tot-=j
        # print(jmp)
        riempiDx(v,jmp,0,len(v)-1,0)
        print("Case #"+str(i+1)+": ",end='')
        for y in v:
            print(str(y)+" ",end='')
        print('')
