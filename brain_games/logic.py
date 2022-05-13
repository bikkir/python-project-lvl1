import prompt


def run(game):
    print('Welcome to the Brain Games!')
    user_name = prompt.string('May I have your name? ')
    print(f'Hello, {user_name}!')
    print(game.task)
    rounds_num = 3
    while rounds_num > 0:
        text_question, correct_answer = game.generate_question()
        print(f'Question: {text_question}')
        user_answer = prompt.string('Your answer: ')
        if user_answer == correct_answer:
            print('Correct!')
            rounds_num -= 1
        else:
            print(f"'{user_answer}' is wrong answer ;(."
                  f" Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {user_name}!")
            break
    if rounds_num == 0:
        print(f'Congratulations, {user_name}!')
