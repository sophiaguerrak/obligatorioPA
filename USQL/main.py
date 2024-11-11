from parser import parser  
from lexer import lexer

# Test cases
usql_query = [
    "TRAEME TODO DE LA TABLA usuarios DONDE edad > 18;", 
    "TRAEME LOS DISTINTOS nombre DE LA TABLA clientes DONDE ciudad = 'Madrid';",
    "METE EN usuarios (nombre, edad) LOS VALORES ('Juan', 25);",
    "ACTUALIZA empleados SETEA salario = 3000 DONDE puesto = 'ingeniero';",
    "TRAEME TODO DE LA TABLA pedidos MEZCLANDO clientes EN pedidos.cliente_id = clientes.id DONDE clientes.ciudad = 'Barcelona';",
    "TRAEME CONTANDO(TODO) DE LA TABLA ventas AGRUPANDO POR producto WHERE DEL GROUP BY CONTANDO(TODO) > 5;",
    "BORRA DE LA TABLA clientes DONDE edad ENTRE 18 Y 25;",
    "CAMBIA LA TABLA empleados AGREGA LA COLUMNA direccion VARCHAR(255) NO NULO;",
    "CAMBIA LA TABLA empleados ELIMINA LA COLUMNA direccion;"
]

for query in usql_query:
    lexer.input(query)  
    token_list = []  

    for tok in lexer:
        token_list.append(tok)  

    sql_query = parser.parse(query)  
    print(f"USQL Query: {query}")
    print(f"SQL Query: {sql_query}")
    
    print("Tokens:")
    for index, token in enumerate(token_list):
        print(f"Token {index}: {token}")
    print() 
