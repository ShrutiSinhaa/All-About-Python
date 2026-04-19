a=int(input("Enter a number: "))
b= range(a,a*11,a)

for i in range(1,11):
  
    if a*i==25:
        break
    else:
        print(a,"*",i,"=",a*i)
  
        
   