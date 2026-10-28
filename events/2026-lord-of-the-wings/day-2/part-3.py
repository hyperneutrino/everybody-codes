# I guess part 1 wasn't overkill because it works for this part just fine as well. Well, let's make
# our existing solution even shorter.

t=0
for l in open(0):
    p=[[*map(int,k.split(">"))]if">"in k else[*map(int,k.split("<"))][::-1]for k in l.split()]
    b={*sum(p,[])}
    i={k:0 for k in b}
    w={k:[]for k in b}
    for x,y in p:
        w[x]+=[y]
        i[y]+=1
    n=0
    for _ in b:
        q=[k for k in i if i[k]<1][0]
        del i[q]
        n=n*10+q
        for k in w[q]:i[k]-=1
    t+=n
print(t)