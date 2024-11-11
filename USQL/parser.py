import ply.yacc as yacc

from lexer import tokens

# SELECT query 
def p_query_select(p):
    '''query : TRAEME selection_todo selection_distinct selection_contando DE_LA_TABLA table_name optional_join condition optional_group_by optional_having optional_order_by optional_limit SEMICOLON'''
    p[0] = f'SELECT {p[2]}{p[3]}{p[4]} FROM {p[6]} {p[7]} {p[8]} {p[9]}{p[10]}{p[11]}{p[12]}'.strip()

def p_selection_todo(p):
    '''selection_todo : TODO
                      | empty'''
    p[0] = '*' if p[1] == 'TODO' else ''

def p_selection_distinct(p):
    '''selection_distinct : LOS_DISTINTOS column_name
                          | empty'''
    p[0] = f'DISTINCT {p[2]}' if len(p) > 2 else ''

def p_selection_contando(p):
    '''selection_contando : CONTANDO LPAREN TODO RPAREN
                          | empty'''
    p[0] = 'COUNT(*)' if len(p) > 2 else ''

# INSERT query
def p_query_insert(p):
    'query : METE_EN table_name LPAREN column_list RPAREN LOS_VALORES LPAREN value_list RPAREN SEMICOLON'
    p[0] = f"INSERT INTO {p[2]} ({p[4]}) VALUES ({p[8]})"

# UPDATE query 
def p_query_update(p):
    'query : ACTUALIZA table_name SETEA column_name OPERATOR value condition SEMICOLON'
    p[0] = f"UPDATE {p[2]} SET {p[4]} {p[5]} {p[6]} {p[7]}"

# DELETE query 
def p_query_delete(p):
    'query : BORRA_DE_LA_TABLA table_name condition SEMICOLON'
    p[0] = f"DELETE FROM {p[2]} {p[3]}"

# CREATE TABLE query
def p_query_create_table(p):
    'query : CREA_LA_TABLA table_name LPAREN column_definitions RPAREN SEMICOLON'
    p[0] = f"CREATE TABLE {p[2]} ({p[4]})"

# ALTER TABLE query
def p_query_alter_table(p):
    'query : CAMBIA_LA_TABLA table_name add_column drop_column SEMICOLON'
    p[0] = f"ALTER TABLE {p[2]} {p[3]} {p[4]}"

# DROP TABLE query
def p_query_drop_table(p):
    'query : TIRA_LA_TABLA table_name SEMICOLON'
    p[0] = f"DROP TABLE {p[2]}"

def p_optional_join(p):
    '''optional_join : MEZCLANDO table_name EN join_columns DONDE join_condition
                     | empty'''
    p[0] = f"JOIN {p[2]} ON {p[4]} WHERE {p[6]}" if len(p) > 2 else ''

def p_join_columns(p):
    '''join_columns : ID DOT ID OPERATOR ID DOT ID
                    | empty'''
    p[0] = f"{p[1]}.{p[3]} {p[4]} {p[5]}.{p[7]}" if len(p) > 2 else ''

def p_join_condition(p):
    '''join_condition : ID DOT ID OPERATOR STRING
                    | empty'''
    p[0] = f"{p[1]}.{p[3]} {p[4]} {p[5]} " if len(p) >2 else ''

def p_condition(p):
    '''condition : DONDE expression
                | CONTANDO LPAREN TODO RPAREN OPERATOR NUMBER
                | empty'''
    p[0] = f"WHERE {p[2]}" if p[1]=='DONDE' else f"COUNT(*) {p[5]} {p[6]}" if p[1]=='CONTANDO' else ''

def p_expression(p):
    '''expression : ID OPERATOR value
                  | ID PARECIDO_A value
                  | ID ES_NULO
                  | ID NO_NULO
                  | ID ENTRE value Y value
                  | ID EN_ESTO LPAREN value_list RPAREN
                  | EXISTE LPAREN query RPAREN
                  | ID DOT ID OPERATOR STRING'''
    if len(p) == 4 and p[2] == 'OPERATOR':
        p[0] = f"{p[1]} {p[2]} {p[3]}"
    elif len(p) == 4 and p[2] == 'PARECIDO_A':
        p[0] = f"{p[1]} LIKE {p[3]}"
    elif len(p) == 3 and p[1] == 'ES_NULO':
        p[0] = f"{p[1]} IS NULL"
    elif len(p) == 3 and p[1] == 'NO_NULO':
        p[0] = f"{p[1]} IS NOT NULL"
    elif len(p) == 6 and p[2] == 'ENTRE':
        p[0] = f"{p[1]} BETWEEN {p[3]} AND {p[5]}"
    elif len(p) == 5 and p[2] == 'EN_ESTO':
        p[0] = f"{p[1]} IN ({p[4]})"
    elif len(p) == 4 and p[1] == 'EXISTE':
        p[0] = f"EXISTS ({p[3]})"
    elif len(p) == 6 and p[2] == 'DOT':
        p[0] = f"{p[1]}.{p[3]} {p[4]} {p[5]}"
    else:
        p[0] = f"{p[1]} {p[2]} {p[3]}"

def p_add_column(p):
    '''add_column : AGREGA_LA_COLUMNA column_definition
                  | empty'''
    p[0] = f"ADD COLUMN {p[2]}" if len(p) > 2 else ''

def p_drop_column(p):
    '''drop_column : ELIMINA_LA_COLUMNA column_name
                   | empty'''
    p[0] = f"DROP COLUMN {p[2]}" if len(p) > 2 else ''

def p_options_type(p):
    '''options_type : LPAREN NUMBER RPAREN unico_constraint no_nulo_constraint por_defecto_constraint clave_prima_constraint clave_referente_constraint
                    | empty'''
    p[0] = f"({p[2]}) NOT NULL" if len(p) > 2 else ''

def p_unico_constraint(p):
    '''unico_constraint : UNICO
                        | empty'''
    p[0] = f"UNIQUE" if p[1] == 'UNICO' else ''

def p_no_nulo_constraint(p):
    '''no_nulo_constraint : NO_NULO
                          | empty'''
    p[0] = f"NOT NULL" if p[1] == 'NO_NULO' else ''

def p_por_defecto_constraint(p):
    '''por_defecto_constraint : POR_DEFECTO value
                              | empty'''
    p[0] = f"DEFAULT {p[2]}" if len(p) > 2 else ''

def p_clave_prima_constraint(p):
    '''clave_prima_constraint : CLAVE_PRIMA
                              | empty'''
    p[0] = f"PRIMARY KEY" if p[1] == 'CLAVE_PRIMA' else ''

def p_clave_referente_constraint(p):
    '''clave_referente_constraint : CLAVE_REFERENTE
                                  | empty'''
    p[0] = f"FOREIGN KEY" if p[1] == 'CLAVE_REFERENTE' else ''

def p_column_definition(p):
    'column_definition : ID TYPE options_type'
    p[0] = f"{p[1]} {p[2]}{p[3]}".strip()

def p_column_definitions(p):
    '''column_definitions : column_definition
                          | column_definitions COMMA column_definition'''
    p[0] = f"{p[1]}, {p[3]}" if len(p) > 2 else p[1]

def p_column_list(p):
    '''column_list : ID
                   | column_list COMMA ID'''
    p[0] = f"{p[1]}, {p[3]}" if len(p) > 2 else p[1]

def p_value_list(p):
    '''value_list : value
                  | value_list COMMA value'''
    p[0] = f"{p[1]}, {p[3]}" if len(p) > 2 else p[1]

def p_value(p):
    '''value : NUMBER
             | STRING
             | ID'''
    p[0] = p[1]


def p_optional_group_by(p):
    '''optional_group_by : AGRUPANDO_POR column_list
                         | empty'''
    p[0] = f"GROUP BY {p[2]}" if len(p) > 2 else ''


def p_optional_having(p):
    '''optional_having : WHERE_DEL_GROUP_BY condition
                       | empty'''
    p[0] = f" HAVING {p[2]}" if len(p) > 2 else ''


def p_optional_order_by(p):
    '''optional_order_by : ORDENA_POR column_list
                         | empty'''
    p[0] = f"ORDER BY {p[2]}" if len(p) > 2 else ''


def p_optional_limit(p):
    '''optional_limit : COMO_MUCHO NUMBER
                      | empty'''
    p[0] = f"LIMIT {p[2]}" if len(p) > 2 else ''

def p_table_name(p):
    'table_name : ID'
    p[0] = p[1]

def p_column_name(p):
    'column_name : ID'
    p[0] = p[1]

def p_empty(p):
    'empty :'
    p[0] = ''

class ParserError(Exception):
    pass

def p_error(p):
    if p:
        error_message= f"Syntax error at '{p.value}'"
    else:
        error_message="Syntax error at end of input"
    raise ParserError(error_message)


start = 'query'
parser = yacc.yacc()