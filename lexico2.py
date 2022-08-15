from gramatica import gramatica as grama
import re as r

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
    
    def busqueda_General2(texto, gramatica):
        met_Evaluar = r.compile(gramatica)
        v_Encontrados = []

        for palabra in texto:
            n_Variable = met_Evaluar.findall(palabra)
            tamanio = len(n_Variable)

            if tamanio > 0:
                v_Encontrados.append(n_Variable)
                posicion = texto.index(palabra)
                texto.pop(posicion)
        total_Frecuencia = len(v_Encontrados)

        return texto, v_Encontrados, total_Frecuencia
                
    def busqueda_Reservadas(texto):
        texto = texto.split()
        tamanio_Reservadas = len(grama.reservadas)
        n_Texto, reservadas, frecuencia = lexico.busqueda_General(texto, tamanio_Reservadas, grama.reservadas)

        return n_Texto, reservadas, frecuencia
    
    def busqueda_Delimitadores(texto):
        tamanio_Delimitadores = len(grama.delimitadores)
        n_Texto, delimitadores, frecuencia = lexico.busqueda_General(texto, tamanio_Delimitadores, grama.delimitadores)
        
        return n_Texto, delimitadores, frecuencia

    
    def busqueda_Operadores(texto):
        tamanio_Operadores = len(grama.operadores)
        n_Texto, operadores, frecuencia = lexico.busqueda_General(texto, tamanio_Operadores, grama.operadores)

        return n_Texto, operadores, frecuencia

    def busqueda_Variables(texto):
        expresion = grama.variables
        n_Texto, variables, frecuencia = lexico.busqueda_General2(texto,expresion)
        
        return n_Texto, variables, frecuencia
    
    def busqueda_Decimales(texto):
        expresion = grama.decimales
        n_Texto, digitos, frecuencia = lexico.busqueda_General2(texto,expresion)

        return n_Texto, digitos, frecuencia
     
    def busqueda_Enteros(texto):
        expresion = grama.enteros
        n_Texto, digitos, frecuencia = lexico.busqueda_General2(texto,expresion)
        
        return n_Texto, digitos, frecuencia
    
    def busqueda_Errores(texto):
        tamanio = len(texto)
        return tamanio, texto