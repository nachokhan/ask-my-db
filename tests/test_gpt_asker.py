import pytest
from gpt_asker import GPTAsker


@pytest.fixture(scope='module')
def gpt_connector():
    return GPTAsker()


def test_send_prompt(gpt_connector):
    prompt = "Can you generate a SQL query to fetch all users from a database?"
    response = gpt_connector.send_prompt(prompt)
    assert response is not None, "Response should not be None"
    assert "SELECT" in response, "Response should contain a SQL SELECT statement"
