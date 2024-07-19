import psycopg2
import os
from dotenv import load_dotenv

from queriers_db.querier_db import QuerierDB

# Load environment variables from the .env file located in ./.conf/
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '../.conf/.env'))


class QuerierDBPostgres(QuerierDB):
    def __init__(self):
        super().__init__()

    def _set_conecction(self):
        dbname = os.getenv('POSTGRES_DB')
        user = os.getenv('POSTGRES_USER')
        password = os.getenv('POSTGRES_PASSWORD')
        host = os.getenv('POSTGRES_HOST')
        port = os.getenv('POSTGRES_PORT')

        self._connection = psycopg2.connect(
            dbname=dbname,
            user=user,
            password=password,
            host=host,
            port=port
        )

    def _set_schema_query(self):
        self._schema_query = """
            SELECT table_name, column_name, data_type 
            FROM information_schema.columns 
            WHERE table_schema = %s';
            """
        self._schama_query_params = (os.getenv('public'),)
