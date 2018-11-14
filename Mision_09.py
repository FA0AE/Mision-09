# Francisco Ariel Arenas Enciso
# A01369122
# Desarrollo de Misión 9 (listas)

'''Declaración de lista global'''
listaGlobal = [1,2,3,2,4,60,5,8,3,22,44,55]     #Esta lista se usará en todas las funciones


'''Función que recibe una lista y mediante un cliclo 'for' regresa una NUEVA lista 
con solamente los valores pares'''
def extraerPares(listaGlobal):
    listaNueva = []                     #Se crea una lista vacía
    for valor in listaGlobal:           #Ciclo 'for' que recorre a la lista
        if valor % 2 == 0:              #Condición que pregunta respecto a si un número es par o impar
            listaNueva.append(valor)    #La condición se cumple (es par) por lo tanto se añaden los valores a lista
    return(listaNueva)                  #Se regresa el resultado


'''Función que recibe una lista y mediante un ciclo 'for' se coloca en una nueva lista, solamente
los datos mayores respecto al anterior de la lista original'''
def extraerMayorPrevio(listaGlobal):
    listaNueva = []                                       #Se crea la lista vacía
    numeroValoresLista = len(listaGlobal)                 #Se obtiene la longitud de la lista original
    ultimoValor = numeroValoresLista - 1                  #Se obtiene el último término de la lista
    for valor in range (0, ultimoValor):                  #Se recorre cada uno de los elementos de la lista
        if listaGlobal[valor] < listaGlobal[valor+1]:     #Se evalua la condición sobre si el número posterior es mayor
            listaNueva.append(listaGlobal[valor+1])       #Se añade a la nueva lista el valor mayor respecto al anterior
    return (listaNueva)                                   #Se regresa el resultado


'''Función que reibe una lista la cual es analizada mediante varios condicionales 'if' y un ciclo 'for' con 
el fin de regresar en una lista nueva un intercambio de las parejas presentes en la original'''
def intercambiarParejas(listaGlobal):
    listaNueva = []                                 #Se crea una nueva lista
    largoLista = len(listaGlobal)                   #Se obtiene el largo de la lista original

    if largoLista == 0:                             #Condición que evalúa que sucede cuando no hay elementos
        return listaNueva                           #Regresa una lista vacía

    if largoLista == 1:                             #Condición que evalúa que pasa cuando hay un solo valor
        listaNueva.append(listaGlobal[0])           #Se le añade a la lista nueva el valor en cuestión
        return listaNueva                           #Regresa una lista nueva con el mismo índice que la orginal

    for valor in range(1, largoLista, 2):           #Ciclo 'for' que recorre los elementos de dos en dos (pares)
        listaNueva.append(listaGlobal[valor])       #Sucede el cambio de lugares
        listaNueva.append(listaGlobal[valor-1])     #Sucede elcambio de lugares

    if largoLista % 2 != 0:                         #Condición que evalúa al últimoelemento de la lista (debe ser par)
        listaNueva.append(listaGlobal[-1])          #Si no lo es... no cambia

    return listaNueva                               #Devuelve el resultado


'''Función que recibe una lista y ésta es modificada para regresar una lista con la posiión del 
valor máximo y mínimo invertida'''
def intercambiarMM(listaGlobal):
    if len(listaGlobal) < 2:                        #Condición que establece que para hacer algún cambio, la lista debe
        listaGlobal = []                            #de contar con más de un elemento
    else:
        valorMenor = min(listaGlobal)               #Se obtiene el valor mínimo de los índices de la lista
        valorMayor = max(listaGlobal)               #Se obtiene el valor máximo de los índices de la lista
        menor = listaGlobal.index(valorMenor)       #Se busca la posición del elemento menor en la lista
        mayor = listaGlobal.index(valorMayor)       #Se busca la posición del elemento mayor en la lista
        listaGlobal[menor] = valorMayor             #Se modifica la posición del menor por el mayor
        listaGlobal[mayor] = valorMenor             #Se modifica la posición del mayor por el menor
    return (listaGlobal)                            #Regresa el resultado


'''Función que recibe una lista, ésta es copiada con copy() con el fin de poder obtener el promedio
del valor de sus índices'''
def promediarCentro(listaGlobal):
    listaNueva = listaGlobal.copy()             #Se crea la copia de la lista
    if len(listaNueva) <= 2:                    #Condición que establece que debe de haber al menos más de 2 elementos
        return (0)                              #Al no tener más de dos valores, regresa 0
    else:
        valorMaximo = max(listaNueva)           #Se obtiene el valor máximo de la copia de la lista
        valorMMinimo = min(listaNueva)          #Se obtiene el valor mínimo de la copia de la lista
        listaNueva.remove(valorMaximo)          #Se elimina el valor máximo de la copia de la lista
        listaNueva.remove(valorMMinimo)         #Se elimina el valor mínimo de la copia de la lista
        suma = sum(listaNueva)                  #Se suman los elementos no elimandos
        promedio = suma // len(listaNueva)      #Se obtiene el promedio entero
    return(promedio)                        #Regresa el resultado


'''Función que recibe una lista y mediante varias condiciones, un ciclo 'for', regresa una dupla con 
el valor de la desviación estándar de los valores de los ínidies de la lista original'''
def calcularEstadistica(listaGlobal):
    largoLista = len(listaGlobal)                  #Se obtiene el largo de la lista
    duplaInicial = (0, 0)                          #Se crea una variable global (para la función) de la dupla
    suma = sum(listaGlobal)                        #Se guarda en una variable la suma de los elementos de la lista

    if largoLista == 0:                            #Si la lista no tiene elementos...
        return duplaInicial                        #...regresará la dupla creada

    if largoLista != 0:                            #Si sí hay valores dentro de la lista...
        mean = suma / largoLista                   #...se calcula la media

    if largoLista > 1:                                          #Si el largo de la lista resulta mayor a uno
        xi = 0                                                  #Acumulador x de la fórmula
        for numero in listaGlobal:                              #Se recorre a la lista
            xi += (numero - mean) ** 2           #El acumulador toma el valor de los parametros menos la media al cuadrado

        desviacion = ((xi) / (len(listaGlobal) - 1)) ** 0.5     #Se calcula la desviación de acuerdo con la fórmula

    else:
        desviacion = 0                           #En caso de ingresar un valor individual su desviación siempre será 0

    return (mean, desviacion)                    #Regresa el resultado


'''Función que recibe una lista y esta regresa la suma de los valores que no se encuentras a lado del
número 13'''
def calcularSuma(listaGlobal):
    largoLista = len(listaGlobal)  # Se obtiene el largo de la lista
    listaNueva = listaGlobal.copy()  # Se crea una copia de la lista orginal para obtener los valores de índices
    listaDatos = []  # Se crea una lista en donde se guardarán los datos
    valorSuma = 0  # Se asume que el resultado de la suma es de 0

    if listaNueva == []:  # Si no hay parametros que sumar...
        return valorSuma  # ...se regresa 0

    listaNueva.insert(0, 0)  # Se le coloca el valor de 0 a la posición incial
    listaNueva.append(0)  # Se agrega 0 a la lista
    largoNuevaLista = len(listaNueva)  # Se obtiene el largo de la lista actualizada

    if listaNueva[0] != 13:
        listaDatos.append(listaNueva[0])  # Se le pasa a la lista 'datos' el índice 0 de la lista actualizada
    if listaNueva[-1] != 13:
        listaDatos.append(listaNueva[-1])  # Se agrega el último índice de la lista actualizada

    ultimoValorActualizado = largoNuevaLista - 1  # Se crea la variable que almacena el valor del último índice
    for valor in range(1, ultimoValorActualizado):
        if listaNueva[valor] != 13 and listaNueva[valor + 1] != 13 and listaNueva[valor - 1] != 13:
            listaDatos.append(listaNueva[valor])
    listaDatos.remove(listaDatos[0])                    #Se remueve el primer término de la lista actualizada
    listaDatos.remove(listaDatos[0])                    #Se vuelve a eliminar el primer término
    suma = len(listaDatos)                              #Se obtiene el largo de la nueva lista
    for resultado in range(0, suma):
        valorSuma += listaDatos[resultado]              #Se eactuliza el resultado de la suma
    return valorSuma                                    #Regresa el resultado
    


