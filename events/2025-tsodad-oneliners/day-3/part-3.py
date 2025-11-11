print((lambda f:f(f,[*map(int,input().split(","))]))(lambda f,x,a={}:f(f,x[1:],{**a,x[0]:a.get(x[0],0)+1})if x else max(a.values())))
