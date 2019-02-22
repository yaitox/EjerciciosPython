print("determinar si un año es bisiesto o no es bisiesto")

anio=int(input("escriba un año"))
if (anio%4==0 and anio%100!=0) or anio%400==0:
  print("el año es bisiesto")
else:
  print("el año no es bisiesto")