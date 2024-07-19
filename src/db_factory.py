import os
from dotenv import load_dotenv
from querier_db_postgres import QuerierDBPostgres
from querier_db_mysql import QuerierDBMySQL

# Load environment variables from the .env file located in ./.conf/
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '../.conf/.env'))


class DBFactory:
    @staticmethod
    def get_db():
        db_type = os.getenv('DB_TYPE')
        if db_type == 'postgres':
            return QuerierDBPostgres()
        elif db_type == 'mysql':
            return QuerierDBMySQL()
        else:
            raise ValueError(f"Unsupported DB_TYPE: {db_type}")
