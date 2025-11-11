print((lambda x:sum(x[i]==x[j].upper()and x[j]in"abc"for i in range(len(x))for j in range(i+1,len(x))))(input()))
