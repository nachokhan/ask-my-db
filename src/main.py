import json
from queries_core import QueriesCore


with open('examples/prompts.json', 'r') as file:
    data = json.load(file)
    prompts = data['prompts']


queries_core = QueriesCore()
answers = []

for prompt in prompts:
    result = queries_core.answer_user_prompt(prompt)
    answers.append({
        "prompt": prompt,
        "csv": result
    })

with open('examples/answers.json', 'w') as file:
    json.dump(answers, file, indent=4)


if __name__ == '__main__':
    for answer in answers:
        print(answer)
