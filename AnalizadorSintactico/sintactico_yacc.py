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
                    | sentenciaCASE
                    | slicing
                    | sentenciaBegin
                    | sentenciaFuncion
                    | split
                    | push
                    | append
                    | pop

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
    ''' puts : PUTS valor


    '''
def p_reverse(p):
    '''  reverse : CADENA PUNTO REVERSE

    '''
def p_split(p):
    '''
         split : CADENA PUNTO SPLIT PIZQ valorsplit PDER
    '''
def p_push(p) :
    '''
       push : variables PUNTO PUSH PIZQ valor PDER
    '''
def p_append(p) :
    '''
        append : variables PUNTO APPEND PIZQ valor PDER
    '''
def p_pop(p) :
    '''
        pop : variables PUNTO POP  PIZQ valor PDER
            | variables PUNTO POP PIZQ  PDER
    '''
def p_valorsplit(p):
    '''
         valorsplit : CADENA
                    | CADENA COMA ENTERO
    '''
def p_include(p):
    '''
        include : CADENA PUNTO INCLUDE INTERROGACION CADENA
    '''

def p_sentenciaFuncion(p):
    ''' sentenciaFuncion : FUNCION  variables codigo  END
    '''

def p_sentenciaWhile(p):
    '''sentenciaWHILE : WHILE  comparacion DO codigo END
    '''

def p_sentenciaCase(p):
    ''' sentenciaCASE : CASE variables sentenciaWhens ELSE codigo END
    '''

def p_sentenciaWhen(p):
    ''' sentenciaWHEN : WHEN valorSencillo codigo
                        | WHEN valorSencillo THEN codigo
    '''
def p_sentenciaAnd(p):
    ''' sentenciaAND : comparacion AND comparacion
    '''
def p_sentenciaOr(p):
    ''' sentenciaOR : comparacion OR comparacion
    '''
def p_sentenciaWhens(p):
    '''sentenciaWhens : sentenciaWHEN
                |  sentenciaWHEN sentenciaWhens
    '''

def p_valorSencillo(p):
    ''' valorSencillo : ENTERO
                | variables
                | CADENA
                | RANGO
    '''
def p_sentenciaBegin(p):
    '''sentenciaBegin : BEGIN codigo END'''

def p_asignacion(p):
    'asignacion : variables IGUAL expresion'


def p_expresion(p):
    ''' expresion : valor
    '''

def p_slicing(p):
    ''' slicing : variables CIZQ ENTERO
                | variables CIZQ ENTERO COMA ENTERO
                | variables CIZQ RANGO
                | variables CIZQ CADENA
    '''

def p_expresion_aritmetica(p):
    '''expresion : valor operadorMat expresion
                | PIZQ valor operadorMat expresion PDER
    '''

def p_comparacion(p):
    '''comparacion : expresion operadorComp expresion
        | PIZQ expresion PDER operadorComp expresion
        | PIZQ expresion operadorComp expresion PDER
    '''

def p_comparaciones(p):
    ''' comparaciones : comparacion
                      | sentenciaAND
                      | sentenciaOR
    '''

def p_sentenciaBreak(p):
    ''' sentenciaBREAK : BREAK
                        | BREAK variables
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
                | split
                | include
                | reverse
    '''

def p_variables(p):
    """ variables : VARIABLE_LOCAL
                | VARIABLE_GLOBAL
                | VARIABLE_OBJETO
                | VARIABLE_CLASE
                | CONSTANTE
    """
def p_sentenciaIf(p):
    ''' sentenciaIf : IF comparaciones codigo finalIf
    '''

def p_finalIf(p):
    ''' finalIf : END
                | sentenciaBREAK END
    '''

def p_comentarios(p):
    ''' comentarios : COMENTARIO
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
        #print(result.value)
        return result

def leerAlgoritmo(file):
    s = file.read()
    print(s)
    result = parser.parse(s)
    print(result)
    file.close()

archivo1 = open("../archivos/algoritmoLoor.txt")
archivo2 = open("../archivos/algoritmoAsqui.txt")
archivo3 = open("../archivos/algoritmoVilcacundo.txt")

'''leerAlgoritmo(archivo1)
leerAlgoritmo(archivo2)
leerAlgoritmo(archivo3)'''
leerAlgoritmo(archivo2)