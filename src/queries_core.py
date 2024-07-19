from queriers_db.db_factory import DBFactory
from gpt_asker import GPTAsker
import csv
import io
from datetime import datetime


class QueriesCore:
    def __init__(self):
        self._querier_db = DBFactory.get_db()
        self._db_schema = self._get_db_schema()
        self._gpt_asker = GPTAsker()

    def _get_db_schema(self):
        return self._querier_db.get_db_schema()

    def answer_user_prompt(self, user_prompt):
        # Send user prompt and DB schema to GPTAsker
        schema_description = self._format_schema(self._db_schema)
        gpt_prompt = f"Based on the following database schema: {schema_description}, generate a SQL query for: {user_prompt}"
        sql_query = self._gpt_asker.send_prompt(gpt_prompt)

        # Execute the generated SQL query
        result = self._querier_db.execute_query(sql_query)

        # Convert the result to CSV
        csv_text = self._convert_to_csv(result)

        # Write CSV text to file        
        # filename = self._generate_filename("query_result", "csv")
        # self._write_csv_to_file(csv_text, filename)

        return csv_text

    def _format_schema(self, schema):
        # Helper method to format the DB schema for GPT prompt
        formatted_schema = "Tables and columns:\n"
        for table, column, data_type in schema:
            formatted_schema += f"Table: {table}, Column: {column}, Type: {data_type}\n"
        return formatted_schema

    def _convert_to_csv(self, query_result):
        # Helper method to convert query result to CSV
        if not query_result:
            return "No results found."

        output = io.StringIO()
        writer = csv.DictWriter(output, fieldnames=query_result[0].keys())
        writer.writeheader()
        writer.writerows(query_result)

        return output.getvalue()

    def _generate_filename(self, base_name, extension):
        # Helper method to generate filename with timestamp
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        return f"{base_name}_{timestamp}.{extension}"

    def _write_csv_to_file(self, csv_text, filename):
        # Helper method to write CSV text to a file
        with open(filename, 'w', newline='') as file:
            file.write(csv_text)
