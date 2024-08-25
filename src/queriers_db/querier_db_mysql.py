import mysql.connector
import os
from dotenv import load_dotenv

from queriers_db.querier_db import QuerierDB

# Load environment variables from the .env file located in ./.conf/
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '../.conf/.env'))


class QuerierDBMySQL(QuerierDB):
    def __init__(self):
        """
        Initializes the QuerierDBMySQL with MySQL connection parameters.
        """
        super().__init__()

    def _set_connection(self):
        """
        Sets up the MySQL connection.
        """
        dbname = os.getenv('MYSQL_DB')
        user = "root"
        password = os.getenv('MYSQL_ROOT_PASSWORD')
        host = os.getenv('MYSQL_HOST')
        port = os.getenv('MYSQL_PORT')

        self._connection = mysql.connector.connect(
            database=dbname,
            user=user,
            password=password,
            host=host,
            port=port
        )

    def _set_schema_query(self):
        """
        Sets the schema query for MySQL.
        """
        self._schema_query = """
            SELECT table_name, column_name, data_type
            FROM information_schema.columns
            WHERE table_schema = %s;
            """
        self._schama_query_params = (os.getenv('MYSQL_DB'),)
