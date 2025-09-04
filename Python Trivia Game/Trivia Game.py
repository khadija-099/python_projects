#list of questions
#store the answers
#randomly pick questions
#ask the questions
#see if they are correct
#keep track of the score
#tell the user their score




import random

questions = {
    "Who developed Python programming language?": "Guido van Rossum",
    "In which year was Python first released?": "1991",
    "What is the file extension of a Python file?": ".py",
    "What keyword is used to define a function in Python?": "def",
    "Which keyword is used to create a class in Python?": "class",
    "What is the output of print(type(10))?": "<class 'int'>",
    "What data type is the result of 3 / 2 in Python 3?": "float",
    "Which function is used to get the length of a list in Python?": "len()",
    "What is the output of bool(\"\")?": "False",
    "Which operator is used for exponentiation in Python?": "**",
    "What keyword is used to handle exceptions in Python?": "try and except",
    "Which built-in function is used to convert a string to an integer?": "int()",
    "What is the correct syntax to import a module named math?": "import math",
    "What is the output of print(\"Hello\" * 3)?": "HelloHelloHello",
    "Which keyword is used to exit a loop in Python?": "break",
    "What is the difference between is and == in Python?": "== checks values, is checks identity (memory address)",
    "Which function is used to read input from the user?": "input()",
    "What is the default value of the end parameter in the print() function?": "\\n",
    "Which Python data type is mutable: tuple or list?": "list",
    "What does PEP stand for in Python?": "Python Enhancement Proposal"
}

def python_trivia_game():
    questions_list = list(questions.keys())
    total_questions = 5
    score = 0

    selected_questions = random.sample(questions_list, total_questions)
    for idx, question in enumerate(selected_questions):
        print(f"{idx+1}. {question}")
        user_answer = input("Your answer: ").lower().strip()
        corrected_answer = questions[question]
        if user_answer == corrected_answer:
            print("Correct!\n")
            score += 1
        else: 
            print(f"Wrong! The correct answer is {corrected_answer}.\n")
    print(f"Game Over! Your score is {score}/ {total_questions}.\n")

    

python_trivia_game()