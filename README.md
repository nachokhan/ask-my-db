
# Ask My DB

## Introduction

NO MORE SQL FOR YOU!

![Example Image](img/example1.png)

Welcome to **Ask My DB**, an innovative project designed to interact with PostgreSQL and MySQL databases using natural language prompts. This project leverages the power of OpenAI's GPT-4 to generate SQL queries based on user input and seamlessly executes these queries on your database. The results are then formatted into a CSV file for easy consumption.

## Features

- **Natural Language Processing**: Generate SQL queries using GPT-4 based on user prompts.
- **Database Integration**: Connects to PostgreSQL and MySQL databases, retrieves schema information, and executes queries.
- **CSV Export**: Converts query results into CSV files with unique timestamps to avoid overwriting.
- **Modular Design**: Clean separation of concerns with dedicated classes for database interaction, GPT query generation, and core logic handling.

## Project Structure

```plaintext
project_directory/
├── .conf/
│   └── .env.template
├── src/
│   ├── __init__.py
│   ├── gpt_asker.py
│   ├── querier_db.py
│   ├── queries_core.py
│   ├── main.py
│   ├── visual/
│   │   ├── ansi_colors.py
│   │   └── ascii_table.py
│   └── queriers_db/
│       ├── db_factory.py
│       ├── querier_db.py
│       ├── querier_db_mysql.py
│       └── querier_db_postgres.py
├── tests/
│   ├── __init__.py
│   ├── conftest.py
│   ├── test_gpt_asker.py
│   ├── test_querier_db.py
│   └── test_queries_core.py
├── .gitignore
├── docker-compose.yml
├── requirements.txt
├── setup.py
└── README.md
```

## Getting Started

### Prerequisites

- Python 3.8 or higher
- PostgreSQL or MySQL database
- Docker (optional for running databases locally)
- OpenAI API key

### Installation

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/yourusername/ask-my-db.git
    cd ask-my-db
    ```

2. **Setup Environment**:
    ```bash
    cp .conf/.env.template .conf/.env
    ```

    Edit the `.conf/.env` file to include your database and OpenAI credentials.

3. **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Run the Database**:
    You can either run PostgreSQL or MySQL locally or use Docker:
    ```bash
    docker-compose up -d
    ```

### Usage

1. **Initialize the Database**:
    Ensure your database is set up and has the required tables. You can use the provided migration scripts or set it up manually.

2. **Run the Application**:
    ```bash
    python src/main.py
    ```

3. **Interact with the System**:
    Enter your natural language query when prompted. The system will generate a SQL query, execute it, and save the results to a uniquely named CSV file.
    NOTE: the prompt is being hardcoded in main.py you must modify it here :)

### Example

1. **Create a Prompt**:
    Prompts are read from a JSON file located at `examples/prompts.json` or can be entered manually. The JSON file can contain one or more prompts. If there are no prompts in the file, you will be prompted to enter one manually. Here's an example of multiple prompts in the JSON file:
    ```json
    {
        "prompts": [
            "Get all users with their names and companies they work for.",
            "Get all products with their prices and stock quantities."
        ]
    }
    ```

    If you are entering the prompt manually, you only need to write the prompt directly when prompted by the application, without using JSON format. For example:

    ```plaintext
    Qrite your prompt here:

    Get all users with their names and companies they work for.
    ```

2. **Run the Main Script**:
    When you run the `main.py` script, it will process the prompts, generate SQL queries using GPT-4, execute them, and display the results in an ASCII table format. Additionally, the results will be saved to a CSV file.

    ```bash
    python src/main.py
    ```

3. **Review the Output**:
    The output will be printed on the console as an ASCII table. The generated CSV files will be saved in the specified directory.

    ```plaintext
    PROMPT: Get all users with their names and companies they work for.
    Processing...

    +---------+-------------+
    |   name  |   company   |
    +---------+-------------+
    |  John   |  Company A  |
    |  Jane   |  Company B  |
    +---------+-------------+
    ```

This example demonstrates how to use the system to generate and execute SQL queries based on natural language prompts and how to interpret the results.


## Testing

To run the tests, ensure you have `pytest` installed and run the following command:

```bash
pytest
```

The tests will verify the functionality of the database interactions, GPT prompt handling, and the CSV file generation.

## Contributing

We welcome contributions to enhance the functionality and features of this project. Please fork the repository, create a new branch, and submit a pull request with your changes.

## License

This project is licensed under the MIT License.

## Contact

For any inquiries or support, please reach out to [ignacio.rigoni@gmail.com](mailto:ignacio.rigoni@gmail.com).

---

Thank you for using **Ask My DB**! We hope this tool makes your database interactions more intuitive and efficient. Happy querying!

---

**Author**: Ignacio Rigoni  
**Repository**: [GitHub Repository URL](https://github.com/nachokhan/ask-my-db)
