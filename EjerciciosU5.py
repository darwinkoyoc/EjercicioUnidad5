import re #libreria de expresiones regulares

path = 'Ciclos_Alumnos.java'

try: 
  #lectura del archivo, pasandolo a una variable
  archivo = open(path, 'r')
except:
  print ('El archivo que intentas abrir no existe')
  quit()

texto = ''

#lectura de lineas del archivo para ser pasados a una variable vacia.
for linea in archivo:
  texto += linea

#print(texto)

patron = re.compile("(\w+( |)=( |)[\d+\.\d+|\w]+)")
result = re.findall(patron, texto) #busca las coincidencias y devuelve un arreglo
print ("\n Ejercicio 1- Sentencia de asignación","\n",result)

patron = r"\w.[\=]{1}\w*.\w*.[+|-|*|/]{1}\w*.\w*.\;"
result = re.findall(patron, texto) #busca las coincidencias y devuelve un arreglo
print ("\n Ejercicio 2- Operaciones aritméticas básicas",result)

patron = r"[a-zA-A]+w*.[==|<=|>=|!=]{2}w*.[a-zA-Z0-9]}"
result = re.findall(patron, texto) #busca las coincidencias y devuelve un arreglo
print ("\n Ejercicio 3 - Expresiones booleanas básicas","\n",result)

patron = r"[a-zA-Z]{1,}[\d|\s]{1,}\=[\s|\w|\d.\d]{1,}[\s|\S][\*|\/|\%|\+|\-][\s|\]\([\w|\d.\d]{1,}[\S|\s][\*|\/|\%|\+|\-][\S|\s][\w|\d.\d]{1,}[ \)|\S\)]\;"
result = re.findall(patron, texto) #busca las coincidencias y devuelve un arreglo
print ("\n Ejercicio 4- Formulas m�s complejas","\n",result)

patron = r"[for|if|while].*[\(]\w.*[\)]\{"
result = re.findall(patron, texto) #busca las coincidencias y devuelve un arreglo
print ("\n Ejercicio 5- El encabezado de estructura","\n",result)
