import mysql.connector
import os
from dotenv import load_dotenv

# Load environment variables from the .env file located in ./.conf/
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '../.conf/.env'))


class QuerierDBMySQL:
    def __init__(self):
        dbname = os.getenv('MYSQL_DB')
        user = "root"
        password = os.getenv('MYSQL_ROOT_PASSWORD')
        host = os.getenv('MYSQL_HOST', 'localhost')
        port = os.getenv('MYSQL_PORT', '3306')

        self._connection = mysql.connector.connect(
            database=dbname,
            user=user,
            password=password,
            host=host,
            port=port
        )

    def get_db_schema(self):
        query = """
        SELECT table_name, column_name, data_type 
        FROM information_schema.columns 
        WHERE table_schema = %s;
        """
        with self._connection.cursor() as cursor:
            cursor.execute(query, (os.getenv('MYSQL_DB'),))
            schema = cursor.fetchall()
        return schema

    def execute_query(self, query):
        with self._connection.cursor() as cursor:
            cursor.execute(query)
            if cursor.description:  # Check if the query returns data
                result = cursor.fetchall()
                column_names = [desc[0] for desc in cursor.description]
                return [dict(zip(column_names, row)) for row in result]
            self._connection.commit()
            return None
