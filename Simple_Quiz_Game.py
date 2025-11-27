print("Simple Quiz Game")
print("------------------")


questions = {
    "What is the capital of France? ": ["Paris"],
    "What is 5+7? ": ["12", "twelve"],
    "What planet is known as the red planet? ": ["Mars"],
    "Which is the largest mammal? ": ["Blue Whale"],
    "What do you get by mixing black and white? ": ["Grey"],
    "How many legs does a horse have? ": ["Four", "4"],
    "The fish walks on land. True or False? ": ["False"]
}

score = 0

for question, answer in questions.items():
    user_answer = input(question)
    if user_answer.strip().lower() in [a.lower() for a in answer]:
        print("Correct!")
        score += 1
    else:
        print(f"Wrong! The correct answer is {answer[0]}.")

print(f"\nYou got {score} out of {len(questions)} correct!")
