import os
from dotenv import load_dotenv
from queriers_db.querier_db import QuerierDB
from queriers_db.querier_db_postgres import QuerierDBPostgres
from queriers_db.querier_db_mysql import QuerierDBMySQL

# Load environment variables from the .env file located in ./.conf/
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '../.conf/.env'))


class DBFactory:
    @staticmethod
    def get_db() -> QuerierDB:
        """
        Returns the appropriate QuerierDB instance based on the DB_TYPE environment variable.

        Returns:
            QuerierDB: An instance of a QuerierDB subclass.

        Raises:
            ValueError: If the DB_TYPE is unsupported.
        """
        querier_db = None
        db_type = os.getenv('DB_TYPE')
        if db_type == 'postgres':
            querier_db = QuerierDBPostgres()
        elif db_type == 'mysql':
            querier_db = QuerierDBMySQL()
        else:
            raise ValueError(f"Unsupported DB_TYPE: {db_type}")

        return querier_db
