
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


    variables = '^[A-Z|a-z][_\d|_A-Za-z]+$'
    decimales = '\d+.\d+'
    enteros = '\d+'