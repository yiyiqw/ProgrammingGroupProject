import random

def ask_question(question, correct_answer):
    print(f"What is the capital of {question}?")
    user_answer = input("Your answer: ").strip().capitalize()

    if user_answer == correct_answer:
        print("Correct! You earned 1 point.")
        return 1
    else:
        print(f"Wrong! The correct answer is {correct_answer}. No points earned.")
        return 0

countries_and_capitals = {
    "Canada": "Ottawa",
    "France": "Paris",
    "Germany": "Berlin",
    "Spain": "Madrid",
    "China": "Beijing",
    "Italy": "Rome",
    "Australia": "Canberra",
    "Austria": "Vienna",
    "Chile": "Santiago",
    "Cuba": "Havana",
    "Norway": "Oslo"
}

questions = list(countries_and_capitals.keys())
random.shuffle(questions)

score = 0
for question in questions:
    score += ask_question(question, countries_and_capitals[question])

percentage = (score / len(questions)) * 100
print(f"\nYour final score is: {score} out of {len(questions)}. Your percentage is: {percentage}")

if percentage >= 90:
    print("Congratulations! You excellent at this!")
elif percentage >= 80:
    print("Congratulations! You are quite good at this!.")
elif percentage >= 70:
    print("Congratulations! You are good at this.")
elif percentage >= 50:
    print("Congratulations! You passed.")
else:
    print("You have failed... Better luck next time :(")
