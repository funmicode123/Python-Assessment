def check_response():
    while True:
        response = input().strip().upper()
        if response in ['A', 'B']:
            return response
        else:
            print("Invalid input. Please enter 'A' or 'B'.")


def print_extrovert_introvert(user_responses, questions):
    e_count = 0
    i_count = 0

    for index in range(0, len(questions), 4):
        selected_option = questions[index][0] if user_responses[index] == 'A' else questions[index][1]
        print(f"Q{index + 1}: {selected_option}")

        if user_responses[index] == 'A':
            e_count += 1
        else:
            i_count += 1

    print(f"Number of A selected: {e_count}")
    print(f"Number of B selected: {i_count}\n")


def print_sensing_intuition(user_responses, questions):
    s_count, n_count = 0, 0
    for index in range(1, len(questions), 4):
        selected_option = questions[index][0] if user_responses[index] == 'A' else questions[index][1]
        print(f"Q{index + 1}: {selected_option}")

        if user_responses[index] == 'A':
            s_count += 1
        else:
            n_count += 1

    print(f"Number of A selected: {s_count}")
    print(f"Number of B selected: {n_count}\n")


def print_thinking_feeling(user_responses, questions):
    t_count, f_count = 0, 0
    for index in range(2, len(questions), 4):
        selected_option = questions[index][0] if user_responses[index] == 'A' else questions[index][1]
        print(f"Q{index + 1}: {selected_option}")

        if user_responses[index] == 'A':
            t_count += 1
        else:
            f_count += 1

    print(f"Number of A selected: {t_count}")
    print(f"Number of B selected: {f_count}\n")


def print_judging_perceptive(user_responses, questions):
    j_count, p_count = 0, 0
    for index in range(3, len(questions), 4):
        selected_option = questions[index][0] if user_responses[index] == 'A' else questions[index][1]
        print(f"Q{index + 1}: {selected_option}")

        if user_responses[index] == 'A':
            j_count += 1
        else:
            p_count += 1

    print(f"Number of A selected: {j_count}")
    print(f"Number of B selected: {p_count}\n")



name = input("What is your name? ")

e_count = i_count = 0
s_count = n_count = 0
t_count = f_count = 0
j_count = p_count = 0


user_responses = [''] * 20

print(f"\nHello, {name}! Kindly answer each question with 'A' or 'B' to determine your personality.\n")


questions = [
    ["A) Expend energy, enjoy groups", "B) Conserve energy, enjoy one on one"],
    ["A) Interpret literally", "B) Look for meaning and possibilities"],
    ["A) Logical, thinking, questioning", "B) Empathetic, feeling, accommodating"],
    ["A) Organized, orderly", "B) Flexible, adaptable"],
    ["A) More outgoing, think out loud", "B) More reserved, think to yourself"],
    ["A) Practical, realistic, experiential", "B) Imaginative, innovative, theoretical"],
    ["A) Candid, straightforward, frank", "B) Tactful, kind, encouraging"],
    ["A) Plan, schedule", "B) Unplanned, spontaneous"],
    ["A) Seek many tasks, public activities, interaction with others", 
     "B) Seek private, solitary activities with quiet to concentrate"],
    ["A) Standard, usual, conventional", "B) Different, novel, unique"],
    ["A) Firm, tend to criticize, hold the line", "B) Gentle, tend to appreciate, conciliate"],
    ["A) Regulated, structured", "B) Easygoing, 'live and let live'"],
    ["A) External, communicative, express yourself", "B) Internal, reticent, keep to yourself"],
    ["A) Focus on here-and-now", "B) Look to the future, global perspective, 'big picture'"],
    ["A) Tough-minded, just", "B) Tender-hearted, merciful"],
    ["A) Preparation, plan ahead", "B) Go with the flow, adapt as you go"],
    ["A) Active, initiate", "B) Reflective, deliberate"],
    ["A) Facts, things, 'what is'", "B) Ideas, dreams, 'what could be', philosophical"],
    ["A) Matter-of-fact, issue-oriented", "B) Sensitive, people-oriented, compassionate"],
    ["A) Control, govern", "B) Latitude, freedom"]
]


for index in range(len(questions)):
    print(f"Q{index + 1}: {questions[0]}  {questions[1]}")
    response = check_response()
    user_responses[index] = response

  
if index % 4 == 0:
    if response == 'A':
        e_count += 1
    else:
        i_count += 1
elif index % 4 == 1:
    if response == 'A':
        s_count += 1
    else:
        n_count += 1
elif index % 4 == 2:
    if response == 'A':
        t_count += 1
    else:
        f_count += 1
elif index % 4 == 3:
    if response == 'A':
        j_count += 1
    else:
        p_count += 1

mbti = ''
mbti += 'E' if e_count >= i_count else 'I'
mbti += 'S' if s_count >= n_count else 'N'
mbti += 'T' if t_count >= f_count else 'F'
mbti += 'J' if j_count >= p_count else 'P'


print(f"\nHello {name}, you selected:")
print_extrovert_introvert(user_responses, questions)
print_sensing_intuition(user_responses, questions)
print_thinking_feeling(user_responses, questions)
print_judging_perceptive(user_responses, questions)

print(f"\n{name}, your MBTI type is: {mbti}")
