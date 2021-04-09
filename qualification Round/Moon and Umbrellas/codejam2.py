X = 0
Y = 0
cost = {}
value = {}
def calcolaprezzo(s):
    if(s==''):
        return 0
    prec = s[0]
    p = 0
    for l in s[1:]:
        if(l!=prec):
            p+=value[prec]
        prec=l
    return p
def trimma(s):
    if('C' not in s):
        return ''
    if('J' not in s):
        return ''
    x=0
    while(s[x]=='?'):
        s=s[1:]
    x=len(s)-1
    while(s[x]=='?'):
        s=s[:x]
        x-=1

    iprec=0
    prec = '?'
    dot=False
    x=0
    while(x<len(s)):
        while(s[x]=='?'):
            dot=True
            x+=1
        if(dot==True):
                if(s[x]==prec):
                    s=s[0:iprec+1]+s[x:]
                    x=iprec+1
                dot=False
        iprec=x
        prec=s[x]
        x+=1
    return s


def solve():
    o = str(input()).split(" ")
    cost[int(o[0])]='J'
    cost[int(o[1])]='C'
    value['C'] = int(o[0])
    value['J'] = int(o[1])
    s = trimma(o[2])
    c = cost[min(cost.keys())]
    s = s.replace("?",c)
    return calcolaprezzo(s)

T = int(input())
for i in range(T):
    print("Case #"+str(i+1)+": "+str(solve()))
