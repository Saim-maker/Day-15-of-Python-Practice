# Python Quiz Game

questions = (
    "How many elements are in vowels?: ",
    "Hottest planet in the solar system?: ",
    "Number of bones in the human body?: ",
    "Biggest continent in the world?: ",
    "Human body temperature?: "
)

options = (
    ("A. 3", "B. 4", "C. 5", "D. 6"),
    ("A. Earth", "B. Venus", "C. Jupiter", "D. Uranus"),
    ("A. 206", "B. 130", "C. 120", "D. 110"),
    ("A. Asia", "B. Europe", "C. Africa", "D. North America"),
    ("A. 30°C", "B. 20°C", "C. 27°C", "D. 37°C")
)

answers = ("C", "B", "A", "A", "D")

guesses = []
score = 0
question_number = 0

for question in questions:
    print("------------------------")
    print(question)

    for option in options[question_number]:
        print(option)

    guess = input("Enter the option (A, B, C, D): ").upper()
    guesses.append(guess)

    if guess == answers[question_number]:
        score += 1
        print("✅ Correct!")
    else:
        print("❌ Wrong!")
        print(f"The correct answer is {answers[question_number]}.")

    question_number += 1

print("\n-------- RESULTS --------")
print("Your guesses:", guesses)
print("Correct answers:", answers)

percentage = (score / len(questions)) * 100
print(f"Your score: {score}/{len(questions)}")
print(f"Percentage: {percentage:.0f}%")


questions = ("Capital of Pakistan?: ",
             "Largest ocean on Earth?: ",
             "Fastest land animal?: ",
             "Which planet is known as the Red Planet?: ",
             "Which gas do plants absorb?: ")
options = (
     ("A. Lahore", "B. Karachi", "C. Islamabad", "D. Peshawar"),
     ("A. Atlantic", "B. Indian", "C. Pacific", "D. Artic"),
     ("A. Lion", "B. Tiger", "C. Cheetah", "D. Horse"),
     ("A. Earth", "B. Mars", "C. Venus", "D. Saturn"),
     ("A. Oxygen", "B. Nitrogen", "C. Carbon Dioxide", "D. Hydrogen")
)

answers = ("C", "C", "C", "B", "C")
guesses = []
score = 0
question_no = 0


for question in questions:
    print(question)
    for option in options[question_no]:
        print(option)

    guess = input("Guess the asnwer: ").upper()
    guesses.append(guess)
    if guess in answers[question_no]:
        score += 1
        print("Correct!")
    else:
        print("Wrong!")
        print(f"The correct answer is {answers[question_no]}")
    question_no += 1

