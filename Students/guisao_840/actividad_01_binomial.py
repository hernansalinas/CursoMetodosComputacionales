def factorial(n):
  if n>0:
    for i in range(1,n):
      n=n*i
    return(n)

def binomial(n,k):
  rest=n-k
  bn= (factorial(n))/((factorial(k))*(factorial(rest)))
  return bn

binomial(7,2)
