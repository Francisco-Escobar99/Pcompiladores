from gramatica import gramatica as grama

tamanio_Reservadas = len(grama.reservadas)

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
                
        print(texto)
        print(newReservadas)
        print(tablaFinal)
        print(totalFrecuencia)

        return texto, reservadas, totalFrecuencia


# lexico.busqueda_Reservadas('Proceso numero , Caracter Real 34 Real 77 , Hacer Logico Real Logico Mexico FinProceso')
            
        