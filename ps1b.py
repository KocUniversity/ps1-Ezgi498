n, B = list(map(int, input().strip().split()))
low=0 #minimum possible value for T
high=10000 #maximum possible value for T
i=1
add=0
a=[] #list to collect all possible T values

while (high-low)!=1: #stops the loop after finding the minimum T 
  T=(high+low)//2 #middle value
  while i<=n: #calculates the equation
     if i%2==0:
       add+=((2**i+1)**(n-i))*T   
     else:
       add+=((3**i+1)**(n-i))*T  
     i+=1
  if add<B: 
      low=T   #chooses the rigt region
  else:
      high=T  #chooses the left region
      a.append(T) #lists the all T values that satisfy the eqaution
  i=1
  add=0
else:
  T=a[-1] #gives the minimum T value that satisfy the equation
  print(T)