print((lambda x:sum(x[i]=="A"and x[j]=="a"for i in range(len(x))for j in range(i+1,len(x))))(input()))
