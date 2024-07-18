from queries_core import QueriesCore

# Example usage
if __name__ == '__main__':
    queries_core = QueriesCore()
    # prompt = "Get all users with their names and companies they work for."
    # result = queries_core.answer_user_prompt(prompt)
    # print(result)
    # print("--------------------")
    prompt2 = "Get the compnies order by number of employees which are older than 70 years old."
    result2 = queries_core.answer_user_prompt(prompt2)
    print(result2)
