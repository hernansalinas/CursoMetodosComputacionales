def lucas(n):
  l1=2 #primer termino de la sucesion
  l2=1 #segundo termino del a sucesion
  for i in range(0,n-1):
    sum=l1+l2
    l1=l2
    l2=sum
  return(sum)

lucas(5)
