# Yacc example

import ply.yacc as yacc

# Get the token map from the lexer.  This is required.
from main import tokens

'''Reglas agregadas por Bryan Loor
p_codigo 
p_algoritmo
p_asignacion
p_sentenciaWhile
p_expresion
p_operadorComp
p_variables
'''

def p_codigo(p):
    '''codigo : algoritmo
                | algoritmo codigo

    '''

def p_algoritmo(p):
    ''' algoritmo : asignacion
                    | expresion
                    | comparacion
                    | sentenciaWHILE

    '''

def p_sentenciaWhile(p):
    '''sentenciaWHILE : WHILE  comparacion DO codigo END
    '''


def p_asignacion(p):
    '''asignacion : variables IGUAL expresion

                    '''

def p_expresion(p):
    '''expresion : valor

    '''
def p_expresion_aritmetica(p):
    'expresion : valor operadorMat expresion'

def p_comparacion(p):
    'comparacion : expresion operadorComp expresion'

def p_operadorMat(p):
    '''operadorMat : MAS
                | RESTA
                | PROD
                | DIVISION
    '''
def p_operadorComp(p):
    '''operadorComp : MAYOR
                | MENOR
                | IGUAL
                | DIFERENTE
    '''


def p_valor(p):
    '''valor : ENTERO
                | variables
    '''

def p_variables(p):
    """ variables : VARIABLE_LOCAL
                | VARIABLE_GLOBAL
                | VARIABLE_OBJETO
                | VARIABLE_CLASE
                | CONSTANTE
    """

# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!")


# Build the parser
parser = yacc.yacc()
'''
while True:
    try:
        s = input('calc > ')
    except EOFError:
        break
    if not s: continue
    result = parser.parse(s)
    print(result)
'''
f=open("../archivos/algoritmoLoor.txt")
s = f.read()
print(s)
result = parser.parse(s)
print(result)
f.close()

