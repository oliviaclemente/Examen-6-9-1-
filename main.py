#ejercicio 1: Al realizar una consulta en un registro hemos obtenido una cadena de texto corrupta al revés. Al parecer contiene el nombre de un alumno y la nota de un exámen. ¿Cómo podríamos formatear la cadena y conseguir una estructura como la siguiente?Nombre Apellido ha sacado un Nota de nota.AyudaPara voltear una cadena rápidamente utilizando slicing podemos utilizar un tercer índice -1: cadena[::-1], 
print("ejercicio 1")
cadena = "zeréP nauJ,01"
l= cadena[::-1].split(",")
print(l[1] + " ha sacado un "+ l[0] +" de nota")
print("")

#ejercicio 2:Realiza un programa que cumpla el siguiente algoritmo utilizando siempre que sea posible operadores en asignación: Guarda en una variable numero_magico el valor 12345679 (sin el 8) Lee por pantalla otro numero_usuario, especifica que sea entre 1 y 9 Multiplica el numero_usuario por 9 en sí mismo Multiplica el numero_magico por el numero_usuario en sí mismo Finalmente muestra el valor final del numero_magico por pantalla
print("ejercicio 2:")
numero_magico = 12345679
numero_usuario = int( input( "Introduce un entero (1-9): "))
numero_usuario *= 9
numero_magico *= numero_usuario
print( numero_magico)
print("")

#ejercicio3:Dadas dos listas, debes generar una tercera con todos los elementos que se repitan en ellas, pero no debe repetirse ningún elemento en la nueva lista:
print("ejercicio3")
lista_1 = ["h",'o','l','a',' ', 'm','u','n','d','o']
lista_2 = ["h",'o','l','a',' ', 'l','u','n','a']
lista_3=[]
for letra in lista_1:
  if letra in lista_2 and letra not in lista_3:
    lista_3.append(letra)
print(lista_3)
print("")

#ejercicio 4: Durante la planificación de un proyecto se han acordado una lista de tareas. Para cada una de estas tareas se ha asignado un orden de prioridad (cuanto menor es el número de orden, más prioridad). ¿Eres capaz de crear una estructura del tipo cola con todas las tareas ordenadas pero sin los números de orden?Sugerencia. Para ordenar automáticamente una lista es posible utilizar el método .sort(), deberias probarlo.
print("ejercicio 4")
from queue import PriorityQueue
class Curso(object):
  def _init_(self, prioridad, nombre):
    self.prioridad = prioridad
    self.nombre = nombre
  def _lt_(self,otro):
    return self.prioridad < otro.prioridad 
cursos = PriorityQueue()
cursos.put(Curso(3, "Python"))
cursos.put(Curso(10, "C++"))
cursos.put(Curso(1, "Algoritmia"))

while not cursos.empty():
  c= cursos.get()
  print(c.prioridad, c.nombre)
print("")

#ejercicio 5: Crea un script llamado descomposicion.py que realice las siguientes tareas: Debe tomar 1 argumento que será un número entero positivo. En caso de no recibir un argumento, debe mostrar información acerca de cómo utilizar el script. El objetivo del script es descomponer el número en unidades, decenas, centenas, miles... tal que por ejemplo si se introduce el número 3647: python descomposicion.py 3647 El programa deberá devolver una descomposición línea a línea como la siguiente utilizando las técnicas de formateo: 0007, 0040, 0600, 3000 Pista Que el valor sea un número no significa necesariamente que deba serlo para formatearlo. Necesitarás jugar muy bien con los índices y realizar muchas conversiones entre tipos cadenas, números y viceversa
print("ejercicio 5")
import sys

if len(sys.argv) == 2:
    numero = int(sys.argv[1])
    if numero < 0 or numero > 9999:
        print("Error - Número es incorrecto")
        print("Ejemplo: descomposicion.py [0-9999]")
    else:
        cadena = str(numero)
        longitud = len(cadena)

        for i in range(longitud):
            print( "{:04d}".format( int(cadena[longitud-1-i]) * 10 ** i ))

else:
    print("Error - Argumentos incorrectos")
    print("Ejemplo: descomposicion.py [0-9999]")

#ejercicio 6: Realiza una función separar(lista) que toma una lista de números enteros y devuelve dos listas ordenadas. La primera con los números pares y la segunda con los números impares.
print("ejercicio 6")
def separar(lista):
  pares= []
  impares= []
  for i in lista:
    if i%2 == 0:
      pares.append(i)
    else: 
      impares.append(i)
  pares.sort()
  impares.sort()
  return pares, impares
  
lista = [6,5,2,1,7]
pares, impares = separar(lista)
print('Pares: ', pares)
print('Impares: ', impares)
print("")

#ejercicio 7: Realizar una función llamada agregar_una_vez(lista, el) que reciba una lista y un elemento. La función debe añadir el elemento al final de la lista con la condición de no repetir ningún elemento. Además, si este elemento ya se encuentra en la lista se debe invocar un error de tipo ValueError que debes capturar y mostrar este mensaje en su lugar:Error: Imposible añadir elementos duplicados => [elemento].Cuando tengas la función intenta añadir los siguientes valores a la lista 10, -2, “Hola” y luego muestre su contenido.
print("ejercicio 7")
elementos = [1, 5, -2]
def agregar_una_vez(elemento):
  if elemento in elementos:
    print(f"Error al añadir elementos duplicados => {elemento}")
  else: 
    elementos.append(elemento)
    
agregar_una_vez(1)
print(elementos)
print("")

#ejercicio8: Utilizando todo lo que sabes sobre cadenas, listas, sus métodos internos… Transforma este texto: Un día el viento soplaba con fuerza#mira cómo se mueve aquella banderola-dijo un monje#lo que se mueve es el viento -respondió otromonje#ni las banderolas ni el viento, lo que se mueve son vuestras mentes – dijo el maestro En este otro: Un día que el viento soplaba con fuerza… - Mira cómo se mueve aquella banderola – dijo un monje. - Lo que se mueve es el viento – respondió otro monje. - Ni las banderolas ni el viento, lo que se mueve son vuestras mentes – dijo el maestro. Lo único prohibido es modificar directamente el texto.
print("ejercicio8")
texto= "Un día el viento soplaba con fuerza#mira cómo se mueve aquella banderola-dijo un monje#lo que se mueve es el viento -respondió otromonje#ni las banderolas ni el viento, lo que se mueve son vuestras mentes – dijo el maestro"
lineas = texto.split("#")
for i, linea in enumerate(lineas):
    lineas[i]= linea.capitalize()
    if i == 0:
      lineas[i] = lineas[i] + "..."
    else: 
      lineas[i] = "-" + lineas[i] + "."
for linea in lineas:
  print(linea)
print("")

#ejercicio 9: Crea una función modificar() que a partir de una lista de números realice las siguientes tareas sin modificar la original: •	Borrar los elementos duplicados •	ordenar la lista de mayor a menor •	eliminar todos los números impares •	realizar una suma de todos los números que quedan •	añadir como primer elemento de la lista la suma realizada •	devolver la lista modificada •	finalmente, después de ejecutar la función, comprueba que la suma de todos los números a partir del segundo, concuerdan con el primer número de la lista tal que así: nueva_lista= modificar(lista) print(nueva_lista[0]==sum(nueva_lista[1:])) True Recordatorio La función sum(lista) devuelve una suma de los elementos de una lista.
print("ejercicio 9:")
lista = [29, -5, -12, 17, 5, 24, 5, 12, 23, 16, 12, 5, -12, 17]

def modificar(l):
  
    l = list(set(l))  
    l.sort(reverse=True)  
 
    l_tmp = []  
    for n in l:
        if n%2 == 0:
            l_tmp.append(n)
            
    suma = sum(l_tmp)  
    l_tmp.insert(0, suma)  
    return l_tmp  


nueva_lista = modificar(lista)
print( nueva_lista[0] == sum(nueva_lista[1:]))
print("")