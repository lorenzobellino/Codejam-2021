iteration = 0
T = int(input())
for i in range(T):
    iteration = 0
    N = input()
    v = [int(x) for x in input().split(" ")]
    for z in range(0,len(v)-1):
        j = v.index(min(v[z:len(v)]))
        v = v[0:z] + list(reversed(v[z:j+1])) + v[j+1:len(v)]
        iteration+=(j-z+1)
    print("Case #"+str(i+1)+": "+str(iteration))
