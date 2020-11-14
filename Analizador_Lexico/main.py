import ply.lex as lex
reserved = {
    "alias": "ALIAS",
    "and": "AND",
    "break": "BREAK",
    "case": "CASE",
    "while":"WHILE",
    "end":"END",
    "do":"DO",
    "def":"FUNCION",
    "else":"ELSE",
    "if":"IF",
    "or":"OR",
    "puts":"PUTS"
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
    "MENOR",
    "MAYOR",
    "CADENA",
    "CIZQ",
    "CDER",
    "ARRAY",
    "LIZQ",
    "LDER",
    "PIZQ",
    "PDER"

] + list(reserved.values())

t_IGUAL= r"="
t_MAS = r"\+"
t_ENTERO = r"\d+"
t_RESTA=r"-"
t_AND=r"&&"
t_MENOR=r"<"
t_MAYOR=r">"
t_CADENA= r'"[a-zA-Z0-9\s]*"'
t_CIZQ = r"\["
t_CDER = r"\]"
t_LIZQ = r"\{"
t_LDER = r"\}"
t_PIZQ = r"\("
t_PDER = r"\)"
t_ARRAY = r"\[(('([a-zA-z\s])*'|[0-9]+|[0-9]+,?[0-9]*),?)+\]"
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

