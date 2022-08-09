from gramatica import gramatica as grama

tamanio_Reservadas = len(grama.reservadas)
tamanio_Delimitadores = len(grama.delimitadores)
tamanio_Operadores = len(grama.operadores)

class lexico:

    def busqueda_Reservadas(texto):
        texto = texto.split()
        tamanio_Texto = len(texto)

        totalFrecuencia = 0
        reservadas = []
        newReservadas = []
        frecuencia_Reservadas = []
        
        for _ in range(tamanio_Texto):
            for numero2 in range(tamanio_Reservadas):
                if grama.reservadas[numero2] in texto:
                    encontrada = grama.reservadas[numero2]
                    newReservadas.append(encontrada)
                    posicion = texto.index(encontrada)
                    texto.pop(posicion)
                
        for palabras in newReservadas:
            frecuencia_Reservadas.append(newReservadas.count(palabras))
        
        for palabra in newReservadas:
            if palabra not in reservadas:
                reservadas.append(palabra)

        tablaFinal = zip(reservadas,frecuencia_Reservadas)
        tablaFinal = tuple(tablaFinal)

        for valor in range(len(tablaFinal)):
            totalFrecuencia = totalFrecuencia + tablaFinal[valor][1]
                
        # print(texto)
        # print(newReservadas)
        # print(tablaFinal)
        # print(totalFrecuencia)

        return texto, reservadas, totalFrecuencia
    
    def busqueda_Delimitadores(texto):
        texto = texto.split()
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
            
        
        # print(texto)
        # print(newDelimitadores)
        # print(tablaFinal)
        # print(total_Frecuencia)

        return texto, delimitadores, total_Frecuencia

    
    def busqueda_Operadores(texto):
        pass

    def busqueda_Variables(texto):
        pass

    def busqueda_Digitos(texto):
        pass
        
        
        
        
lexico.busqueda_Delimitadores('Hola == como estas < >=')
# lexico.busqueda_Reservadas('Proceso numero , Caracter Real 34 Real 77 , Hacer Logico Real Logico Mexico FinProceso')
            
        