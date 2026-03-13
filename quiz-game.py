import random

# List of questions (you can add more later)
questions = [
    {"question": "What does CPU stand for?",
     "options": ["a) Central Processing Unit", "b) Computer Personal Unit", "c) Central Program Utility"],
     "answer": "a"},

    {"question": "Which language is used for AI?",
     "options": ["a) Python", "b) HTML", "c) CSS"],
     "answer": "a"},

    {"question": "What does RAM stand for?",
     "options": ["a) Random Access Memory", "b) Read Access Memory", "c) Rapid Application Method"],
     "answer": "a"},

    {"question": "Which symbol is used for Python comments?",
     "options": ["a) //", "b) #", "c) /* */"],
     "answer": "b"},

    {"question": "What does GPU stand for?",
     "options": ["a) Graphics Processing Unit", "b) General Program Unit", "c) Graph Utility Program"],
     "answer": "a"},

    {"question": "What is the brain of the computer?",
     "options": ["a) CPU", "b) RAM", "c) Hard Drive"],
     "answer": "a"},

    {"question": "Which device stores data permanently?",
     "options": ["a) RAM", "b) Hard Drive", "c) CPU"],
     "answer": "b"},


     {"question": "What does IDE stand for?",
      "options": ["a) Integrated Development Environment", "b) Internal Data Engine", "c) Integrated Design Element"],
      "answer": "a"},

     {"question": "Which Python function is used to display output?",
      "options": ["a) display()", "b) print()", "c) show()"],
      "answer": "b"},

     {"question": "Which symbol is used to compare equality in Python?",
      "options": ["a) =", "b) ==", "c) ==="],
      "answer": "b"},

     {"question": "Which loop repeats while a condition is true?",
      "options": ["a) for loop", "b) repeat loop", "c) while loop"],
      "answer": "c"},

     {"question": "Which device is used to input text into a computer?",
      "options": ["a) Monitor", "b) Keyboard", "c) Printer"],
      "answer": "b"},

     {"question": "What is the main circuit board of a computer called?",
      "options": ["a) Motherboard", "b) Processor board", "c) Main chip"],
      "answer": "a"},

     {"question": "Which storage device is faster?",
      "options": ["a) HDD", "b) SSD", "c) DVD"],
      "answer": "b"},

     {"question": "Which network connects computers worldwide?",
      "options": ["a) LAN", "b) Internet", "c) PAN"],
      "answer": "b"},

     {"question": "Which programming language is known for its snake logo?",
      "options": ["a) Java", "b) Python", "c) C++"],
      "answer": "b"},

     {"question": "What does URL stand for?",
      "options": ["a) Universal Resource Locator", "b) Uniform Resource Locator", "c) United Resource Link"],
      "answer": "b"},

     {"question": "Which component temporarily stores running programs?",
      "options": ["a) RAM", "b) Hard drive", "c) SSD"],
      "answer": "a"},

     {"question": "Which key is used to start a new line when typing?",
      "options": ["a) Shift", "b) Enter", "c) Tab"],
      "answer": "b"},

    {"question": "Which device is used to move the cursor on a computer screen?",
     "options": ["a) Mouse", "b) Printer", "c) Scanner"],
     "answer": "a"},

    {"question": "Which language is mainly used for styling web pages?",
     "options": ["a) CSS", "b) Python", "c) SQL"],
     "answer": "a"},

    {"question": "Which type of memory is non-volatile?",
     "options": ["a) RAM", "b) ROM", "c) Cache"],
     "answer": "b"},

     {"question": "Which data type is used to store True or False values in Python?",
 "options": ["a) bool", "b) string", "c) float"],
 "answer": "a"},

{"question": "What does IDE stand for?",
 "options": ["a) Integrated Development Environment", "b) Internal Data Engine", "c) Integrated Design Element"],
 "answer": "a"},

{"question": "Which Python function is used to display output?",
 "options": ["a) display()", "b) print()", "c) show()"],
 "answer": "b"},

{"question": "Which symbol is used to compare equality in Python?",
 "options": ["a) =", "b) ==", "c) ==="],
 "answer": "b"},

{"question": "Which loop repeats while a condition is true?",
 "options": ["a) for loop", "b) repeat loop", "c) while loop"],
 "answer": "c"},

{"question": "Which device is used to input text into a computer?",
 "options": ["a) Monitor", "b) Keyboard", "c) Printer"],
 "answer": "b"},

{"question": "What is the main circuit board of a computer called?",
 "options": ["a) Motherboard", "b) Processor board", "c) Main chip"],
 "answer": "a"},

{"question": "Which storage device is faster?",
 "options": ["a) HDD", "b) SSD", "c) DVD"],
 "answer": "b"},

{"question": "Which network connects computers worldwide?",
 "options": ["a) LAN", "b) Internet", "c) PAN"],
 "answer": "b"},

{"question": "Which programming language is known for its snake logo?",
 "options": ["a) Java", "b) Python", "c) C++"],
 "answer": "b"},

{"question": "What does URL stand for?",
 "options": ["a) Universal Resource Locator", "b) Uniform Resource Locator", "c) United Resource Link"],
 "answer": "b"},

{"question": "Which component temporarily stores running programs?",
 "options": ["a) RAM", "b) Hard drive", "c) SSD"],
 "answer": "a"},

{"question": "Which key is used to start a new line when typing?",
 "options": ["a) Shift", "b) Enter", "c) Tab"],
 "answer": "b"},

{"question": "Which device is used to move the cursor on a computer screen?",
 "options": ["a) Mouse", "b) Printer", "c) Scanner"],
 "answer": "a"},

{"question": "Which language is mainly used for styling web pages?",
 "options": ["a) CSS", "b) Python", "c) SQL"],
 "answer": "a"},

{"question": "Which type of memory is non-volatile?",
 "options": ["a) RAM", "b) ROM", "c) Cache"],
 "answer": "b"},
]
import random
# Randomly pick 8 questions for this quiz
quiz_questions = random.sample(questions, 8)
score = 0

print("Welcome to the Computer Science Quiz!")
print("--------------------------------------")

# Quiz loop
for q in quiz_questions:
    print("\n" + q["question"])

    for option in q["options"]:
        print(option)

    answer = input("Your answer: ").lower()

    if answer == q["answer"]:
        print("Correct!")
        score += 1
    else:
        print("Wrong!")

print("\nYour score:", score)

# Read previous high score
import os

# file name
filename = "highscore.txt"

# create file if it doesn't exist
if not os.path.exists(filename):
    with open(filename, "w") as file:
        file.write("0")

# read high score
with open(filename, "r") as file:
    highscore = int(file.read())

if score > highscore:
    print("New High Score!")
    with open("highscore.txt", "w") as file:
        file.write(str(score))
else:
    print("High Score remains:", highscore)
    input("\nPress Enter to exit...")