class USQLQuery:
    def __init__(self):
        self.query = ""

    def traeme(self, selection='*'):
        self.query += f"SELECT {selection} "
        return self

    def de_la_tabla(self, table_name):
        self.query += f"FROM {table_name} "
        return self

    def donde(self, condition):
        self.query += f"WHERE {condition} "
        return self

    def los_distintos(self, selection):
        self.query = f"SELECT DISTINCT {selection} " + self.query[len("SELECT "):]
        return self

    def mete_en(self, table_name):
        self.query += f"INSERT INTO {table_name} "
        return self
    
    def valores(self, values):
        self.query += f"VALUES {values} "
        return self
    
    def actualiza(self, table_name):
        self.query += f"UPDATE {table_name} "
        return self
    
    def setea(self, update_list):
        self.query += f"SET {update_list} "
        return self
    
    def contando(self, selection):
        self.query += f"COUNT {selection} "
        return self
    
    def agrupando_por(self, selection):
        self.query += f"GROUP BY {selection} "
        return self
    
    def where_del_group_by(self, condition):
        self.query += f"HAVING {condition} "
        return self
    
    def borra_de_la(self, table_name):
        self.query += f"DELETE FROM {table_name} "
        return self
    
    def cambia_la_tabla(self, table_name):
        self.query += f"ALTER TABLE {table_name} "
        return self
    
    def agrega_la_columna(self, column_definition):
        self.query += f"ADD COLUMN {column_definition} "
        return self
    
    def elimina_la_columna(self, column_name):
        self.query += f"DROP COLUMN {column_name} "
        return self

    def build(self):
        return self.query.strip() + ";"