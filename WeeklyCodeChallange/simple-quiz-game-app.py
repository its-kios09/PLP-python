# Simple Quiz Game 🎮
# Create a multiple-choice quiz with questions about Python, movies, or any fun topic!
# Display scores at the end and allow the user to play again. 🏆

def simple_game():
    questions = {
        "Inbuilt name for a function is called?": "def",
        "What is the number one top series on Netflix?": "Stranger Things",  # Updated answer for accuracy
    }
    score = 0

    for question, answer in questions.items():
        print(f'\n{question}')
        user_answer = input("Your answer: ").strip()
        if user_answer.lower() == answer.lower():
            print("Correct! 🎉")
            score += 1
        else:
            print(f"Wrong! The correct answer was: {answer}.")

    print(f"\nYour final score: {score}/{len(questions)}")

    play_again = input("Play again? (yes/no): ").strip().lower()
    if play_again == "yes":
        simple_game()
    else:
        print("Thanks for playing! 👋")

simple_game()