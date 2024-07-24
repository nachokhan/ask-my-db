import json
import os
from queries_core import QueriesCore
from visual.ascii_table import csv_string_to_ascii_table
from visual.ansi_colors import ANSI_COLORS


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

    queries_core = QueriesCore()
    answers = []

    if prompts == []:
        prompts.append(input("Escribi tu consulta aca:\n\n"))
        clear_screen()

    for prompt in prompts:
        print(f"\n{ANSI_COLORS["bg_bright_black"]}#########################################################################################\n{ANSI_COLORS["reset"]}")
        print(f"{ANSI_COLORS["yellow"]}PROMPT{ANSI_COLORS["reset"]}: {ANSI_COLORS["cyan"]}{prompt}{ANSI_COLORS["reset"]}")
        print("Processing...")
        result = queries_core.answer_user_prompt(prompt)
        answers.append({
            "prompt": prompt,
            "csv": result
        })
        table = csv_string_to_ascii_table(result, "blue", "green", "green")
        print("\033[F\033[K", end='')
        print(f"\n{table}")

    with open('examples/answers.json', 'w') as file:
        json.dump(answers, file, indent=4)
