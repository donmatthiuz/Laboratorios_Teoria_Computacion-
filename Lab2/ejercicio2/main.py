#Ejercicio 2 Laboratorio 2. 
from parse import parsechain, determinate_balance


cadena = " a ( a | b ) * b + a ?"
cadena2= " ( ( a | b ) b ) * [ az ] b ]"
cadena3= " ( a * b * c * d * ( a | e | i | o | u ) ) e * f * g * h ) { 1 , 2 }"
cadena4 = "^ [ aZ ] . com { 5 , 30 }"
cadena5 = "( [ [ az ] [ AZ ] ] ( ( ( ( ( . | ; ) | ; ) | . ) | . ) | . ) { 10 , 20 } ) ∗ ) +"
cadenas = cadena.split(" ")
cadenas2 = cadena2.split(" ")
cadenas3 = cadena3.split(" ")
cadenas4 = cadena4.split(" ")
cadenas5 = cadena5.split(" ")
print(parsechain(cadenas5))
cl = parsechain(cadenas5)
determinate_balance(cl)

