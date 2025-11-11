print((lambda x:(lambda f:f(f,[[*map(int,k.split())]for k in x]))(lambda f,x,t=100:f(f,x[1:],t*x[0][0]/x[0][1])if x else int(t)))(open(0).read().split("|")))
