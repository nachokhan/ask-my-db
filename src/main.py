from queries_core import QueriesCore

# Example usage
if __name__ == '__main__':
    queries_core = QueriesCore()
    # prompt = "Get all users with their names and companies they work for."
    # result = queries_core.answer_user_prompt(prompt)
    # print(result)
    # print("--------------------")
    prompt2 = """
NEcesito una tabla que me permita saber en que horarios (divididos entre 'Mañana' 'Tarde' y 'Noche') la gente se dedica a sacar reservas para ir al 'Origen de i'.
ME gustaria una tabla de doble entrada donde las columnas sean los horarios y las filas sean los años 2021 al 2024.
La mañana se considera desde las 6 hasta las 11:59
LA tarde desde las 12pm hasta las 19.
La noche desde las 19 hasta las 3. de la mañana.
Lo ideal es que los valores esten en porcentajes respecto de los horarios para cada año.
"""
    result2 = queries_core.answer_user_prompt(prompt2)
    print(result2)
