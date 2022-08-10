
class gramatica:

    reservadas = [
        'Algortimo',
        'Cadena',
        'Caracter',
        'Como',
        'Con Paso',
        'De Otro Modo',
        'Definir',
        'Dimension',
        'Entero',
        'Entonces',
        'Escribir',
        'Falso',
        'FinAlgoritmo',
        'FinFuncion',
        'FinMientras',
        'FinPara',
        'FinSegun',
        'FinSi',
        'FinSubProceso',
        'Funcion',
        'Hacer',
        'Hasta Que',
        'Leer',
        'Logico',
        'Mientras',
        'Para',
        'Por Referencia',
        'Por Valor',
        'Real',
        'Segun',
        'Si',
        'Sin Saltar',
        'SiNo',
        'SubProceso',
        'Verdadero',
        'Proceso',
        'FinProceso'
    ]

    delimitadores = [
        '==','!=','>','<','>=','<=','<>','[',']','"',','
    ]

    operadores = [
        '+', '-', '*','/', '%','<-','(',')','&','|','~','^'
    ]

    variables = '[a-zA-Z_][a-zA-Z_0-9]*'
    decimales = '\d+\.\d+'
    enteros = '\d+'