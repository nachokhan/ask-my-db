

class QuerierDB:
    def __init__(self):
        self._schema_query = None
        self._schama_query_params = None

        self._set_conecction()
        self._set_schema_query()

    def _set_conecction(self):
        raise Exception("_set_conecction() method not implemented!")

    def _set_schema_query(self):
        raise Exception("_set_schema_query() method not implemented!")

    def get_db_schema(self):
        with self._connection.cursor() as cursor:
            cursor.execute(self._schema_query, self._schama_query_params)
            schema = cursor.fetchall()
        return schema

    def execute_query(self, query):
        with self._connection.cursor() as cursor:
            cursor.execute(query)
            if cursor.description:
                result = cursor.fetchall()
                column_names = [desc[0] for desc in cursor.description]
                return [dict(zip(column_names, row)) for row in result]
            self._connection.commit()
            return None
