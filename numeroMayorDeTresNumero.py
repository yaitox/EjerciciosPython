print("determinar cual numero es mayor de tres numeros")

num1=int(input("escriba el primer numero"))
num2=int(input("escriba el segundo numero"))
num3=int(input("escriba el tercer numero"))

if num1>num2 and num1>num3:
  print("el numero ",num1," es mayor")
else:
   if num2>1 and num2>num3:
     print("el numero ",num2," es mayor")
   else:
      print("el numero ",num3," es mayor")