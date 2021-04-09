T = int(input())
P = int(input())

for z in range(T):
    risposte= []
    cazzi = []
    for i in range(100):
        ll = str(input())[:1001]
        risposte.append([int(x) for x in ll])
    for r in risposte:
        sum=0
        for c in r:
            sum+=c
        cazzi.append(sum)
    print("Case #"+str(z+1)+": "+str(cazzi.index(max(cazzi))+1))
