# lexer.py
import ply.lex as lex
class LexerError(Exception):
    pass

tokens = [
    'NO_NULO','CAMBIA_LA_TABLA', 'TRAEME', 'TODO', 'DE_LA_TABLA', 'DONDE', 'AGRUPANDO_POR', 
    'MEZCLANDO', 'EN', 'LOS_DISTINTOS', 'CONTANDO', 'METE_EN',
    'LOS_VALORES', 'ACTUALIZA', 'SETEA', 'BORRA_DE_LA_TABLA', 'ORDENA_POR',
    'COMO_MUCHO', 'WHERE_DEL_GROUP_BY', 'EXISTE', 'EN_ESTO',
    'ENTRE', 'PARECIDO_A', 'ES_NULO', 'AGREGA_LA_COLUMNA', 
    'ELIMINA_LA_COLUMNA', 'CREA_LA_TABLA', 
    'TIRA_LA_TABLA', 'POR_DEFECTO', 'UNICO', 'CLAVE_PRIMA', 
    'CLAVE_REFERENTE', 'TRANSFORMA_A',
    'Y', 'O', 'ID', 'OPERATOR', 'NUMBER', 'STRING', 'COMMA', 
    'SEMICOLON', 'LPAREN', 'RPAREN', 'DOT', 'ASTERISK','DE', 'TYPE'
]

t_ignore = ' \t'
t_CAMBIA_LA_TABLA = r'\bCAMBIA\s*LA\s*TABLA\b'
t_TRAEME = r'\bTRAEME\b'
t_TODO = r'\bTODO\b'
t_DE_LA_TABLA = r'\bDE\s*LA\s*TABLA\b'
t_DONDE = r'\bDONDE\b'
t_AGRUPANDO_POR = r'\bAGRUPANDO\s*POR\b'
t_MEZCLANDO = r'\bMEZCLANDO\b'
t_EN = r'\bEN\b'
t_LOS_DISTINTOS = r'\bLOS\s*DISTINTOS\b'
t_CONTANDO = r'\bCONTANDO\b'
t_METE_EN = r'\bMETE\s*EN\b'
t_LOS_VALORES = r'\bLOS\s*VALORES\b'
t_ACTUALIZA = r'\bACTUALIZA\b'
t_SETEA = r'\bSETEA\b'
t_BORRA_DE_LA_TABLA = r'\bBORRA\s*DE\s*LA\s*TABLA\b'
t_ORDENA_POR = r'\bORDENA\s*POR\b'
t_COMO_MUCHO = r'\bCOMO\s*MUCHO\b'
t_WHERE_DEL_GROUP_BY = r'\bWHERE\s*DEL\s*GROUP\s*BY\b'
t_EXISTE = r'\bEXISTE\b'
t_EN_ESTO = r'\bEN\s*ESTO\b'
t_ENTRE = r'\bENTRE\b'
t_PARECIDO_A = r'\bPARECIDO\s*A\b'
t_ES_NULO = r'\bES\s*NULO\b'
t_AGREGA_LA_COLUMNA = r'\bAGREGA\s*LA\s*COLUMNA\b'
t_ELIMINA_LA_COLUMNA = r'\bELIMINA\s*LA\s*COLUMNA\b'
t_CREA_LA_TABLA = r'\bCREA\s*LA\s*TABLA\b'
t_TIRA_LA_TABLA = r'\bTIRA\s*LA\s*TABLA\b'
t_POR_DEFECTO = r'\bPOR\s*DEFECTO\b'
t_UNICO = r'\bUNICO\b'
t_CLAVE_PRIMA = r'\bCLAVE\s*PRIMA\b'
t_CLAVE_REFERENTE = r'\bCLAVE\s*REFERENTE\b'
t_NO_NULO = r'NO\s+NULO'
t_TRANSFORMA_A = r'\bTRANSFORMA\s*A\b'
t_Y = r'\bY\b'
t_O = r'\bO\b'
t_OPERATOR = r'[><=]+'
t_STRING = r'\'[^\']*\''
t_COMMA = r','
t_SEMICOLON = r';'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_DOT = r'\.'
t_ASTERISK = r'\*'
t_DE = r'DE'

t_ID = r'[a-z][a-z0-9_]*'
    
t_TYPE = r'INT|VARCHAR|CHAR|FLOAT|DOUBLE|DECIMAL|NUMERIC|DATE|TIME|TIMESTAMP'

t_NUMBER = r'\d+'

def t_error(t):
    error_message = f"Illegal character '{t.value[0]}' at line {t.lineno}, position {t.lexpos}"
    raise LexerError(error_message)

lexer = lex.lex()
