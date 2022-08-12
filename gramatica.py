
class gramatica:

    reservadas = [
        'Caracter',
        'Como',
        'Definir',
        'Entero',
        'Escribir',
        'Falso',
        'Leer',
        'Logico',
        'Real',
        'Verdadero',
        'Proceso',
        'FinProceso'
    ]

    delimitadores = [
        '[',']','"',',','(',')','.'
    ]

    operadores = [
        '+', '-', '*','/','<-'
    ]


    variables = '[a-zA-Z_][a-zA-Z_0-9]*'
    decimales = '\d+\.\d+'
    enteros = '\d+'