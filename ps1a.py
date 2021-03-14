n, B = list(map(int, input().strip().split()))
T=0
i=1
add=0

while T<=10000:
   T+=1
   while i<=n: #calculates the equation
     if i%2==0:
       add+=((2**i+1)**(n-i))*T     
     else:
       add+=((3**i+1)**(n-i))*T  
     i+=1
   
   if add<B: #to find the minimum T value that satisfies the equation
      i=1
      add=0
   else:
      break
if T>10000: #to specify the signal "not found"
    print('-1')
else:
    print(T)
    
    