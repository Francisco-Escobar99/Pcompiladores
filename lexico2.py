from gramatica import gramatica as grama

tamanio_Reservadas = len(grama.reservadas)

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


# lexico.busqueda_Reservadas('Proceso numero , Caracter Real 34 Real 77 , Hacer Logico Real Logico Mexico FinProceso')
            
        