a=float(input("Enter a number"))
b=float(input("Enter another number"))
o=str(input("Enter the operator"))
if o!=str("+") and o!=str("-") and o!=str("*") and o!=("/") and o!=str("**") and o!=str("//"):
  print("Wrong operator")
elif o==str("+"):
  r=a+b
  print(a,"+",b,"=",r)
elif o==str("-"):
  r=a-b
  print(a,"-",b,"=",r)
elif o==str("*"):
  r=a*b
  print(a,"x",b,"=",r)
elif o==str("/"):
  r=a/b
  print(a,"/",b,"=",r)
elif o==str("**"):
  r=a**b
  print(a,"^",b,"=",r)
elif o==str("//"):
  r=a//b
  print(a,"//",b,"=",r)