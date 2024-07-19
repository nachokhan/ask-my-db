import pytest
from queriers_db.db_factory import DBFactory


@pytest.fixture(scope='module')
def querier_db():
    db = DBFactory.get_db()
    yield db
    # Clean up after tests
    db.execute_query('DROP TABLE IF EXISTS test_table;')


@pytest.fixture(scope='module', autouse=True)
def setup_database(querier_db):
    # Create a generic test table
    querier_db.execute_query('''
    CREATE TABLE IF NOT EXISTS test_table (
        id INT PRIMARY KEY AUTO_INCREMENT,
        data VARCHAR(100)
    );
    ''')
    yield
    # Clean up after tests
    querier_db.execute_query('DROP TABLE IF EXISTS test_table;')


def test_get_db_schema(querier_db):
    schema = querier_db.get_db_schema()
    assert len(schema) > 0, "Schema should not be empty"

    # Check if the test_table is in the schema
    tables = [table[0] for table in schema]
    assert 'test_table' in tables, "test_table should be in the schema"


def test_execute_query(querier_db):
    # Insert test data
    querier_db.execute_query('INSERT INTO test_table (data) VALUES (\'Test Data 1\'), (\'Test Data 2\');')

    # Query the test data
    result = querier_db.execute_query('SELECT * FROM test_table')
    assert len(result) == 2, "There should be 2 entries in the test_table"
    assert result[0]['data'] == 'Test Data 1', "First entry's data should be 'Test Data 1'"
    assert result[1]['data'] == 'Test Data 2', "Second entry's data should be 'Test Data 2'"
