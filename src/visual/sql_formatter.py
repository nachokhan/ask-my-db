from pygments import highlight
from pygments.lexers import SqlLexer
from pygments.formatters import TerminalFormatter


class SQLFormatter:
    def __init__(self, tab_size=4):
        self.tab_size = tab_size

    def format_sql(self, sql_query):
        formatted_query = sql_query.replace('\t', ' ' * self.tab_size)
        colorful_query = highlight(formatted_query, SqlLexer(), TerminalFormatter())
        print(colorful_query)


# Ejemplo de uso
if __name__ == "__main__":
    formatter = SQLFormatter(tab_size=4)
    sql_query = """
    SELECT
        column1,
        column2,
        column3
    FROM
        table_name
    WHERE
        condition1 = 'value1'
        AND condition2 = 'value2';
    """
    formatter.format_sql(sql_query)
