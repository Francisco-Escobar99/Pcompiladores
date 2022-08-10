from gramatica import gramatica as grama


tamanio_Delimitadores = len(grama.delimitadores)
tamanio_Operadores = len(grama.operadores)

class lexico:

    def busqueda_General(texto, tamanio, t_Gramatica):
        tamanio_Texto = len(texto)

        total_Frecuencia = 0
        encontradas = []
        nuevo_Texto = []
        frecuencias = []

        for _ in range(tamanio_Texto):
            for numero in range(tamanio):
                if t_Gramatica[numero] in texto:
                    encontrada = t_Gramatica[numero]
                    nuevo_Texto.append(encontrada)
                    posicion = texto.index(encontrada)
                    texto.pop(posicion)
        
        for palabras in nuevo_Texto:
            frecuencias.append(nuevo_Texto.count(palabras))
        
        for palabra in nuevo_Texto:
            if palabra not in encontradas:
                encontradas.append(palabra)
        
        datos_Finales = zip(encontradas, frecuencias)
        datos_Finales = tuple(datos_Finales)

        for valor in range(len(datos_Finales)):
            total_Frecuencia += datos_Finales[valor][1]
        
        return texto, encontradas, total_Frecuencia


    def busqueda_Reservadas(texto):
        texto = texto.split()
        tamanio_Reservadas = len(grama.reservadas)
        n_Texto, reservadas, frecuencia = lexico.busqueda_General(texto, tamanio_Reservadas, grama.reservadas)

        return n_Texto, reservadas, frecuencia
    
    def busqueda_Delimitadores(texto):
        tamanio_Texto = len(texto)
        
        total_Frecuencia = 0
        delimitadores = []
        newDelimitadores = []
        frecuencia_Delimitadores = []

        for _ in range(tamanio_Texto):
            for numero in range(tamanio_Delimitadores):
                if grama.delimitadores[numero] in texto:
                    encontrada = grama.delimitadores[numero]
                    newDelimitadores.append(encontrada)
                    posicion = texto.index(encontrada)
                    texto.pop(posicion)
        
        for simbolo in newDelimitadores:
            frecuencia_Delimitadores.append(newDelimitadores.count(simbolo))
        
        for delimitador in newDelimitadores:
            if delimitador not in delimitadores:
                delimitadores.append(delimitador)
        
        tablaFinal = zip(delimitadores,frecuencia_Delimitadores)
        tablaFinal = tuple(tablaFinal)
        tamanio = len(tablaFinal)

        for valor in range(tamanio):
            total_Frecuencia += tablaFinal[valor][1]

        return texto, delimitadores, total_Frecuencia

    
    def busqueda_Operadores(texto):
        tamanio_Texto = len(texto)

        total_Frecuencias = 0 

    def busqueda_Variables(texto):
        pass

    def busqueda_Digitos(texto):
        pass
        