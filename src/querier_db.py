import psycopg2
import os
from dotenv import load_dotenv

# Load environment variables from the .env file located in ./.config/
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '../.conf/.env'))


class QuerierDB:
    def __init__(self):
        dbname = os.getenv('POSTGRES_DB')
        user = os.getenv('POSTGRES_USER')
        password = os.getenv('POSTGRES_PASSWORD')
        host = os.getenv('POSTGRES_HOST', 'localhost')
        port = os.getenv('POSTGRES_PORT', '5432')

        self._connection = psycopg2.connect(
            dbname=dbname,
            user=user,
            password=password,
            host=host,
            port=port
        )

    def get_db_schema(self):
        query = """
        SELECT table_name, column_name, data_type 
        FROM information_schema.columns 
        WHERE table_schema = 'public';
        """
        with self._connection.cursor() as cursor:
            cursor.execute(query)
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
