import re
archivo=open('datos.txt','r')
mensaje=archivo.read()


print("por favor ingresa un una opcion")
print("1: variables validas")
print("2: enteros y decimales")
print("3: operadores aritmeticos")
print("4: operadores relacionales")
print("5: palabras reservadas")
numero = int(input())
5
if numero==1:
	patron = re.compile('\s[A-Za-z]+\;')
	print (patron.findall(mensaje))
	archivo.close()
#---------------------------------------------------------

if numero==2:
	patron = re.compile('\s([0-9]+(\d+)?\;|\d+\.+\d+\;)')
	print (patron.findall(mensaje))
	archivo.close()
#---------------------------------------------------------

if numero==3:
	patron = re.compile('[+*/-]')
	print (patron.findall(mensaje))
	archivo.close()
#---------------------------------------------------------

if numero==4:
	patron = re.compile('[<>=\!]')
	print (patron.findall(mensaje))
	archivo.close()

#---------------------------------------------------------
if numero==5:
	patron = re.compile('if|else|double|print')
	print (patron.findall(mensaje))
	archivo.close()

