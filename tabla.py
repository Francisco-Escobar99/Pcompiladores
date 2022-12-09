class tablaAnalisis:
    diccionario = {
       'G' : {'produccion': ['BLOQUE4', 'BLOQUE3', 'BLOQUE2', 'BLOQUE1']},
       'BLOQUE1' : {'produccion': ['L', 'Proceso']},
       'L': {'produccion': ['Letra']},
        'Letra': {'produccion': ['a...z']},
        'BLOQUE2': {'produccion': ['TD', 'C', 'L', 'Definir']},
        # 'VP': {'produccion': ['L', ',']},
        'C': {'produccion': ['Como']},
        'TD': {'produccion': ['Entero'] },
        'BLOQUE3': {'produccion': ['Contenido2','Valor', '<-', 'L']},
        'Contenido2': {'produccion': ['L', 'Leer', '"', 'L', '"', 'Escribir']},
        'Valor': {'produccion': ['D']},
        'D': {'produccion': ['0...9']},
        'BLOQUE4': {'produccion': ['FinProceso']},
    }
