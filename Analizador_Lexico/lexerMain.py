import ply.lex as lex
reserved = {
    "alias": "ALIAS",
    "break": "BREAK",
    "case": "CASE",
    "while":"WHILE",
    "end":"END",
    "do":"DO",
    "def":"FUNCION",
    "else":"ELSE",
    "in": "IN",
    "if":"IF",
    "puts":"PUTS",
    "for":"FOR",
    "unless":"UNLESS",
    "=begin" :"BEGINC",
    "=end" :"ENDC"

}
tokens = [
    "VARIABLE_GLOBAL",
    "VARIABLE_LOCAL",
    "VARIABLE_OBJETO",
    "VARIABLE_CLASE",
    "CONSTANTE",
    "COMP_IGUAL",
    "IGUAL",
    "DIFERENTE",
    "ENTERO",
    "MAS",
    "RESTA",
    "MENOR",
    "MAYOR",
    "CADENA",
    "POTENCIA",
    "DIVISION",
    "CIZQ",
    "CDER",
    "ARRAY",
    "HASH",
    "LIZQ",
    "LDER",
    "PIZQ",
    "PDER",
    "RANGO",
    "AND",
    "OR",
    "PROD",
    "COMENTARIOL"



] + list(reserved.values())
t_AND=r"&&"
t_OR=r"\|\|"
t_IGUAL= r"="
t_COMP_IGUAL=r"=="
t_DIFERENTE=r"!="
t_MAS = r"\+"
t_ENTERO = r"\d+"
t_RESTA=r"-"
t_MENOR=r"<"
t_MAYOR=r">"
t_CADENA= r'"[a-zA-Z0-9\s,]*"'
t_PROD =r"\*"
t_POTENCIA = r"\*\*"
t_DIVISION=r"/"
t_CIZQ = r"\["
t_CDER = r"\]"
t_LIZQ = r"\{"
t_LDER = r"\}"
t_PIZQ = r"\("
t_PDER = r"\)"
t_RANGO= r"\.\."
t_ARRAY = r"\[(('([a-zA-z\s])*'|[0-9]+|[0-9]+,?[0-9]*),?)+\]"
t_HASH = r"\{((\"|')?[a-zA-Z_][a-zA-Z0-9_\s]*(\"|')?(\:|\=>)([0-9]|[1-9][0-9]*|(\"|')[\w\s]+(\"|')),?)+\}"
t_COMENTARIOL = r"\#.*"

def t_CONSTANTE(t):
    r"[A-Z][a-zA-Z0-9_]*"
    t.type = reserved.get(t.value, 'CONSTANTE')  # Check for reserved words
    return t
def t_VARIABLE_LOCAL(t):
    r"[a-z_][a-zA-Z0-9_]*"
    t.type = reserved.get(t.value, 'VARIABLE_LOCAL')  # Check for reserved words
    return t
def t_VARIABLE_OBJETO(t):
    r"@[a-zA-Z_][a-zA-Z0-9_]*"
    t.type = reserved.get(t.value, 'VARIABLE_OBJETO')  # Check for reserved words
    return t
def t_VARIABLE_CLASE(t):
    r"@@[a-zA-Z0-9_]*"
    t.type = reserved.get(t.value, 'VARIABLE_CLASE')  # Check for reserved words
    return t
def t_VARIABLE_GLOBAL(t):
    r"\$[a-zA-Z0-9_]*"
    t.type = reserved.get(t.value, 'VARIABLE_GLOBAL')  # Check for reserved words
    return t
def t_newline(t):
    r"\n+"
    t.lexer.lineno += len(t.value)
t_ignore = ' \t'
def t_error(t):
    print("No es reconocido '%s'" % t.value[0])
    t.lexer.skip(1)
lexer = lex.lex()

def analizar(data):
    lexer.input(data)
    # Tokenize
    while True:
        tok = lexer.token()
        if not tok:
            break  # No more input
        print(tok)


'''
def leerText(txt):
    data=txt.split("\n")
    for linea in data:
        print(">>")
        if len(linea)==0:
            break
        return analizar(linea)
'''

def leer(file):
    for linea in file:
        print(">>" + linea)
        analizar(linea)
        if len(linea) == 0:
            break

archivo1 = open("../archivos/ejemplosVilcacundo.txt")
archivo2 = open("../archivos/ejemplosLoor.txt")
archivo3 = open("../archivos/ejemplosAsqui.txt")
'''
leer(archivo1)
leer(archivo2)
leer(archivo3)
'''

