import ply.lex as lex
reserved = {
    "while":"WHILE",
    "end":"END",
    "do":"DO",
    "def":"FUNCION"
}
tokens = [
    "VARIABLE_GLOBAL",
    "VARIABLE_LOCAL",
    "VARIABLE_OBJETO",
    "VARIABLE_CLASE",
    "CONSTANTE",
    "IGUAL",
    "ENTERO",
    "MAS",
    "RESTA",
    "AND",
    "MENOR"

] + list(reserved.values())

t_IGUAL= r"="
t_MAS = r"\+"
t_ENTERO = r"\d+"
t_RESTA=r"-"
t_AND=r"&&"
t_MENOR=r"<"
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


archivo = open("../archivos/ejemplos.txt")
for linea in archivo:
    print(">>"+linea)
    analizar(linea)
    if len(linea)==0:
        break

