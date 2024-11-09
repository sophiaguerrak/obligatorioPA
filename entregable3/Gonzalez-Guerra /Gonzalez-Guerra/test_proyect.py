import unittest
from fluentAPI import USQLQuery
from lexer import lexer, LexerError, tokens
from parser import parser, ParserError



class TestLexer(unittest.TestCase):
    def test_traeme_todo_query(self):
        lexer.input("TRAEME TODO DE LA TABLA usuarios;")
        tokens = [tok.type for tok in lexer]
        expected_tokens = ['TRAEME', 'TODO', 'DE_LA_TABLA', 'ID', 'SEMICOLON']
        self.assertEqual(tokens, expected_tokens)

    def test_invalid_character(self):
        lexer.input("TRAEME #INVALID")  
        with self.assertRaises(LexerError):
            list(lexer)

class TestParser(unittest.TestCase):

    def test_simple_select_query(self):
        query = "TRAEME TODO DE LA TABLA usuarios DONDE name = roberto;"
        result = parser.parse(query)
        expected_sql = "SELECT * FROM usuarios  WHERE name = roberto"
        self.assertEqual(result, expected_sql)

    def test_insert_query(self):
        query = "METE EN usuarios (nombre, edad) LOS VALORES ('Juan', 25);"
        result = parser.parse(query)
        expected_sql = "INSERT INTO usuarios (nombre, edad) VALUES ('Juan', 25)"
        self.assertEqual(result, expected_sql)

    def test_invalid_query(self):
        query = "TRAEME TODO DE LA TABLA usuarios DONDE name = roberto"
        with self.assertRaises(ParserError):
            parser.parse(query)

    def test_alter_table_query(self):
        query = "CAMBIA LA TABLA empleados AGREGA LA COLUMNA direccion VARCHAR(255) NO NULO;"
        result = parser.parse(query)
        expected_sql = "ALTER TABLE empleados ADD COLUMN direccion VARCHAR(255) NOT NULL "
        self.assertEqual(result, expected_sql)

    def test_drop_table_query(self):
        query = "TIRA LA TABLA empleados;"
        result = parser.parse(query)
        expected_sql = "DROP TABLE empleados"
        self.assertEqual(result, expected_sql)

    def test_values_query(self):
        query = "METE EN usuarios (nombre, edad) LOS VALORES ('Juan', 25);"
        result = parser.parse(query)
        expected_sql = "INSERT INTO usuarios (nombre, edad) VALUES ('Juan', 25)"
        self.assertEqual(result, expected_sql)

    def test_update_query(self):
        query = "ACTUALIZA empleados SETEA salario = 3000 DONDE puesto = 'ingeniero';"
        result = parser.parse(query)
        expected_sql = "UPDATE empleados SET salario = 3000 WHERE puesto = 'ingeniero'"
        self.assertEqual(result, expected_sql)

    def test_delete_query(self):
        query = "BORRA DE LA TABLA clientes DONDE edad ENTRE 18 Y 25;"
        result = parser.parse(query)
        expected_sql = "DELETE FROM clientes WHERE edad BETWEEN 18 AND 25"
        self.assertEqual(result, expected_sql)

    def test_create_table_query(self):
        query = "CREA LA TABLA empleados (id INT, nombre VARCHAR(100));"
        result = parser.parse(query)
        expected_sql = "CREATE TABLE empleados (id INT, nombre VARCHAR(100) NOT NULL)"
        self.assertEqual(result, expected_sql)

    def test_group_by_query(self):
        query = "TRAEME TODO DE LA TABLA usuarios AGRUPANDO POR edad;"
        result = parser.parse(query)
        expected_sql = "SELECT * FROM usuarios   GROUP BY edad"
        self.assertEqual(result, expected_sql)


class TestUSQLFluentAPI(unittest.TestCase):
    def setUp(self):
        self.query = USQLQuery()  

    def test_traeme(self):
        result = self.query.traeme("nombre").build()
        expected = "SELECT nombre;"
        self.assertEqual(result, expected)

    def test_de_la_tabla(self):
        result = self.query.traeme("nombre").de_la_tabla("usuarios").build()
        expected = "SELECT nombre FROM usuarios;"
        self.assertEqual(result, expected)

    def test_donde(self):
        result = self.query.traeme().de_la_tabla("usuarios").donde("edad > 18").build()
        expected = "SELECT * FROM usuarios WHERE edad > 18;"
        self.assertEqual(result, expected)

    def test_los_distintos(self):
        result = self.query.los_distintos("nombre").de_la_tabla("usuarios").build()
        expected = "SELECT DISTINCT nombre FROM usuarios;"
        self.assertEqual(result, expected)

    def test_mete_en(self):
        result = self.query.mete_en("usuarios").valores("(1, 'Juan')").build()
        expected = "INSERT INTO usuarios VALUES (1, 'Juan');"
        self.assertEqual(result, expected)

    def test_actualiza(self):
        result = self.query.actualiza("usuarios").setea("nombre='Juan'").donde("id=1").build()
        expected = "UPDATE usuarios SET nombre='Juan' WHERE id=1;"
        self.assertEqual(result, expected)

    def test_contando(self):
        result = self.query.contando("nombre").de_la_tabla("usuarios").build()
        expected = "COUNT nombre FROM usuarios;"
        self.assertEqual(result, expected)

    def test_agrupando_por(self):
        result = self.query.traeme("nombre").de_la_tabla("usuarios").agrupando_por("edad").build()
        expected = "SELECT nombre FROM usuarios GROUP BY edad;"
        self.assertEqual(result, expected)

    def test_where_del_group_by(self):
        result = self.query.traeme("nombre").de_la_tabla("usuarios").agrupando_por("edad").where_del_group_by(
            "edad > 18").build()
        expected = "SELECT nombre FROM usuarios GROUP BY edad HAVING edad > 18;"
        self.assertEqual(result, expected)

    def test_borra_de_la(self):
        result = self.query.borra_de_la("usuarios").donde("id=1").build()
        expected = "DELETE FROM usuarios WHERE id=1;"
        self.assertEqual(result, expected)

    def test_cambia_la_tabla(self):
        result = self.query.cambia_la_tabla("usuarios").agrega_la_columna("nombre VARCHAR(100)").build()
        expected = "ALTER TABLE usuarios ADD COLUMN nombre VARCHAR(100);"
        self.assertEqual(result, expected)

    def test_elimina_la_columna(self):
        result = self.query.cambia_la_tabla("usuarios").elimina_la_columna("nombre").build()
        expected = "ALTER TABLE usuarios DROP COLUMN nombre;"
        self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()
