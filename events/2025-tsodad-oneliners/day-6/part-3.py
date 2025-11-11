print((lambda x,f:f(x*2)*999-f(x)*998)(input(),lambda k:sum(k[max(i-1000,0):min(i+1001,len(k))].count(k[i].upper())if k[i]in"abc"else 0for i in range(len(k)))))
