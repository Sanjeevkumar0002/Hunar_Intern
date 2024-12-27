# Step 1: Questions and Answers
questions = {
    "What is the capital of France?": "a",
    "Which planet is known as the Red Planet?": "b",
    "What is the largest mammal on Earth?": "c",
    "How many continents are there?": "d",
}

choices = {
    "What is the capital of France?": "a) Paris\nb) Rome\nc) Berlin\nd) Madrid",
    "Which planet is known as the Red Planet?": "a) Venus\nb) Mars\nc) Jupiter\nd) Saturn",
    "What is the largest mammal on Earth?": "a) Elephant\nb) Whale Shark\nc) Blue Whale\nd) Giraffe",
    "How many continents are there?": "a) Five\nb) Six\nc) Seven\nd) Eight",
}

answers = {
    "What is the capital of France?": "a",
    "Which planet is known as the Red Planet?": "b",
    "What is the largest mammal on Earth?": "c",
    "How many continents are there?": "c",
}

# Step 2: Initialize score
score = 0

# Step 3: Loop through questions
print("Welcome to the Quiz!\n")
for question, correct_answer in answers.items():
    print(question)
    print(choices[question])
    user_answer = input("Enter your answer (a/b/c/d): ").lower()

    # Step 4: Provide feedback
    if user_answer == correct_answer:
        print("Correct!\n")
        score += 1
    else:
        print(f"Wrong! The correct answer is '{correct_answer}'.\n")

    print(f"Current Score: {score}/{len(questions)}\n")

# Step 5: End of Quiz
print("Quiz Over!")
print(f"Your Final Score: {score}/{len(questions)}")
if score == len(questions):
    print("Excellent! You got all questions right!")
elif score > len(questions) // 2:
    print("Good Job! Keep practicing!")
else:
    print("Better luck next time!")
