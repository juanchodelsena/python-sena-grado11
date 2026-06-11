#HACER UN PROGRAMA QUE DETERMINE SI UN ESTUDIANTE APRUEBA O DESAPRUEBA CON UN PROMEDIO DE 5 NOTAS ENTREGADAS
print("Este programa retorna el promedio de sus 5 notas")
nota1=int(input("Ingrese su primer nota "))
nota2=int(input("Ingrese su segunda nota "))
nota3=int(input("Ingrese su tercer nota "))
nota4=int(input("Ingrese su cuarta nota "))
nota5=int(input("Ingrese su quinta nota "))
prom=(nota1+nota2+nota3+nota4+nota5)/5
if prom>=3:
      print("Aprobó con un promedio de: ",prom)
else:
     print("Reprobó con un promedio de: ",prom)