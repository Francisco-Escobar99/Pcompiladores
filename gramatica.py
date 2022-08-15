
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


    variables = '^[A-Z|a-z][a-z0-9|a-z\_\d|a-z]+$'
    decimales = '\d+\.\d+'
    enteros = '\d+'