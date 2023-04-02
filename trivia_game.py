import random

class Question:
    def __init__(self, question, options, answer):
        self.question = question
        self.options = options
        self.answer = answer

    def __str__(self):
        return self.question

    def check_answer(self, answer):
        return answer == self.answer

    def display_options(self):
        for i, option in enumerate(self.options):
            print(f"{i + 1}. {option}")

questions = [
    Question("What is the capital of Illinois?", ["Springfield", "London", "Chicago", "Mchenry"], 1),
    Question("What number is Michael Jordan known for?", ["10", "33", "22", "23"], 4),
    Question("What is the term they use for a football?", ["Pigskin", "Ball", "Rock", "Thing"], 1),
    Question("What year did the Chicago Bears win a Super Bowl?", ["2005", "1979", "1985", "1998"], 3),
    Question("Who has the most career points in NBA history?", ["Lebron James", "Kareem", "Jordan", "Malone"], 1),
    Question("Which number does Lebron James wear currently for the Lakers?", ["6", "23", "15", "34"], 1),
    Question("Who did the Chiefs beat in this past Super Bowl?", ["49ers", "Eagles", "Jets", "Packers"], 2),
    Question("Who hit the most home runs in one season for the Chicago Cubs?", ["Sammy Sosa", "Kris Bryant",
                                                                                "Javy Baez", "Mark Grace"], 1),
    Question("Who created Marvel comics?", ["Jeff Bezos", "Stan Lee", "Donald Trump", "Bill Clinton"], 2),
    Question("Who is the author of Harry Potter?", ["J.D. Salinger", "JK Rowling", "F. Scott Fitzgerald", "Mark Twain"]
             , 2)
]

random.shuffle(questions)

print("Welcome to the Trivia Game!")
print("Player 1, please enter your name:")
player1_name = input("> ")
print("Player 2, please enter your name:")
player2_name = input("> ")

player1_score = 0
player2_score = 0

for i, question in enumerate(questions):
    print(f"Question {i+1}: {question}")
    question.display_options()
    answer = int(input("Enter your answer (1-4): "))
    if answer < 1 or answer > 4:
        print("Invalid input. Please enter a number between 1 and 4.")
        continue
    if question.check_answer(answer):
        if i % 2 == 0:
            player1_score += 1
            print(f"Correct! {player1_name} earns a point.")
        else:
            player2_score += 1
            print(f"Correct! {player2_name} earns a point.")
    else:
        print("Incorrect.")

print("Game over!")
print(f"Final score: {player1_name}: {player1_score}, {player2_name}: {player2_score}")

if player1_score > player2_score:
    print(f"{player1_name} wins!")
elif player2_score > player1_score:
    print(f"{player2_name} wins!")
else:
    print("It's a tie!")
