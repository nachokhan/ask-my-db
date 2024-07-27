import json
import os
from gpt_marketing import GPTMarketing
from queries_core import QueriesCore
from visual.ascii_table import csv_string_to_ascii_table
from visual.ansi_colors import COLOR
from visual.markdown_formatter import MarkdownFormatter
from visual.sql_formatter import SQLFormatter


def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


if __name__ == "__main__":

    clear_screen()

    with open('examples/prompts.json', 'r') as file:
        data = json.load(file)
        prompts = data['prompts']

    try:
        queries_core = QueriesCore()
        sql_formatter = SQLFormatter()
        mdown_formatter = MarkdownFormatter()
        gpt_marketing = GPTMarketing()
    except Exception as e:
        print(f"{COLOR["red"]}ERROR{COLOR["reset"]}: {COLOR["yellow"]}{e}{COLOR["reset"]}\n")
        exit()

    if prompts == []:
        prompts.append(input("Write your prompt here:\n\n"))
        clear_screen()

    answers = []

    results_for_marketing = []

    for prompt in prompts:

        result = {}
        try:
            print(f"\n{COLOR["bg_bright_black"]}#########################################################################################\n{COLOR["reset"]}")
            print(f"{COLOR["yellow"]}PROMPT{COLOR["reset"]}: {COLOR["cyan"]}{prompt}{COLOR["reset"]}")
            print("Processing...")
            csv, query = queries_core.answer_user_prompt(prompt)
            result = {
                "prompt": prompt,
                "query": query,
                "csv": csv
            }
            table = csv_string_to_ascii_table(csv, "blue", "green", "green")
            print("\033[F\033[K", end='')
            print(f"\n{table}")
            print(f"\n{COLOR["yellow"]}GENERATED SQL QUERY{COLOR["reset"]}:")
            sql_formatter.format_sql(query)

            results_for_marketing.append(
                {
                    "prompt": prompt,
                    "table": table,
                }
            )

        except Exception as e:
            result = {
                "prompt": prompt,
                "error": e
            }
            print(f"{COLOR["red"]}ERROR{COLOR["reset"]}: {COLOR["yellow"]}{e}{COLOR["reset"]}")

        answers.append(result)

    conclusions = gpt_marketing.analyze_csv_text(results_for_marketing, "marketing")
    print(f"\n{COLOR['yellow']}MARKETING INSIGHTS{COLOR['reset']}:\n\n")
    mdown_formatter.format_markdown(conclusions)

    with open('examples/insights.md', 'w') as file:
        file.write(conclusions)

    with open('examples/answers.json', 'w') as file:
        json.dump(answers, file, indent=4)
