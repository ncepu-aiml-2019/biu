i=2
print("100内的质数有：")
for i in range(2,100):
   j=2
   for j in range(2,i):
      if(i%j==0):
         break
   else:
      print(i,end=" ")
print()

