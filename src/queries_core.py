from querier_db import QuerierDB


class QueriesCore:
    def __init__(self):
        self._querier_db = QuerierDB()
        self._db_schema = self._get_db_schema()

    def _get_db_schema(self):
        return self._querier_db.get_db_schema()

    def answer_user_prompt(self):
        pass

    def _something(self):
        pass
