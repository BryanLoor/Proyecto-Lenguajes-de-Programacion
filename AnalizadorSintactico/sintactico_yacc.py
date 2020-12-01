
import ply.yacc as yacc

# Get the token map from the lexer.  This is required.

from Analizador_Lexico.lexerMain import tokens

'''Reglas agregadas por Bryan Loor
p_codigo 
p_algoritmo
p_asignacion
p_sentenciaWhile
p_expresion
p_operadorComp
p_variables
p_comentarioS
'''
'''Reglas agregadas por Nicole Asqui
p_sentenciaFor 
p_range
p_puts
p_unless
'''
'''Reglas agregadas por Ricardo Vilcacundo
p-sentenciaIf
'''



def p_codigo(p):
    '''codigo : algoritmo
                | algoritmo codigo
    '''
def p_algoritmo(p):
    ''' algoritmo : asignacion
                    | sentenciaWHILE
                    | sentenciaFOR
                    | puts
                    | unless
                    | comentarios
                    | sentenciaIf
    '''

def p_unless(p):
    ''' unless : UNLESS comparacion codigo END
    '''
def p_sentenciaFor(p):
    ''' sentenciaFOR : FOR variables IN range DO codigo END
    '''

def p_range(p):
    ''' range : ENTERO RANGO ENTERO
    '''

def p_puts(p):
    ''' puts : PUTS CADENA
    '''


def p_sentenciaWhile(p):
    '''sentenciaWHILE : WHILE  comparacion DO codigo END
    '''

def p_asignacion(p):
    'asignacion : variables IGUAL expresion'

def p_expresion(p):
    '''expresion : valor
    '''

def p_expresion_aritmetica(p):
    '''expresion : valor operadorMat expresion
                | PIZQ valor operadorMat expresion PDER
    '''

def p_comparacion(p):
    '''comparacion : expresion operadorComp expresion
        | PIZQ expresion PDER operadorComp expresion
    '''


def p_operadorMat(p):
    '''operadorMat : MAS
                | RESTA
                | PROD
                | DIVISION
                | POTENCIA
    '''
def p_operadorComp(p):
    '''operadorComp : MAYOR
                | MENOR
                | COMP_IGUAL
                | DIFERENTE
    '''


def p_valor(p):
    '''valor : ENTERO
                | variables
                | CADENA
                | HASH
                | ARRAY
    '''

def p_variables(p):
    """ variables : VARIABLE_LOCAL
                | VARIABLE_GLOBAL
                | VARIABLE_OBJETO
                | VARIABLE_CLASE
                | CONSTANTE
    """
def p_sentenciaIf(p):
    'sentenciaIf : IF comparacion codigo END'

def p_comentarios(p):
    ''' comentarios : COMENTARIOL
    '''

# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!")


# Build the parser
parser = yacc.yacc()
def crearArchivoSintactico(data):
    file = open("sintactico.txt", "w")
    result = parser.parse(data)
    file.write(str(result))
    file.write("\n")
    file.close()

def reglas():
    file = open("reglas.txt", "w")
    print(parser.productions)
    file.write("Reglas del Lenguaje\n")
    for x in range(0, len(parser.productions)):
        file.write(str(parser.productions[x]))
        file.write("\n")
    file.close()

def leerCodigo(data):
        #print(data)
        result = parser.parse(data)
        print(result)
        return result

'''
def leerAlgoritmo(file):
    s = file.read()
    print(s)
    result = parser.parse(s)
    print(result)
    file.close()
'''
archivo1 = open("../archivos/algoritmoLoor.txt")
archivo2 = open("../archivos/algoritmoAsqui.txt")
archivo3 = open("../archivos/algoritmoVilcacundo.txt")
'''
leerAlgoritmo(archivo1)
leerAlgoritmo(archivo2)
leerAlgoritmo(archivo3)
'''
