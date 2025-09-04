from flask import Flask, render_template_string, request, session, redirect, url_for
import random

app = Flask(__name__)
app.secret_key = "my_secret_key"  # session ke liye zaroori

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

# HTML template (no separate file needed)
template = """
<!DOCTYPE html>
<html>
<head>
    <title>🐍 Python Trivia Game</title>
</head>
<body style="font-family:Arial; text-align:center; margin-top:50px;">
    <h1>🐍 Python Trivia Game</h1>

    {% if not game_over %}
        <h2>Q{{ q_num }}: {{ question }}</h2>
        <form method="post">
            <input type="text" name="answer" placeholder="Your Answer" required>
            <button type="submit">Submit</button>
        </form>

        {% if feedback %}
            <p><b>{{ feedback }}</b></p>
            <form method="post" action="{{ url_for('next_question') }}">
                <button type="submit">Next Question</button>
            </form>
        {% endif %}
    {% else %}
        <h2>🎉 Game Over!</h2>
        <p>Your final score: {{ score }}/5</p>
        <form method="post" action="{{ url_for('restart') }}">
            <button type="submit">Play Again</button>
        </form>
    {% endif %}
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def index():
    if "questions" not in session:
        session["questions"] = random.sample(list(questions.keys()), 5)
        session["q_index"] = 0
        session["score"] = 0
        session["feedback"] = ""

    q_index = session["q_index"]

    if request.method == "POST" and "answer" in request.form:
        user_answer = request.form["answer"].strip().lower()
        correct_answer = questions[session["questions"][q_index]].lower()

        if user_answer == correct_answer:
            session["score"] += 1
            session["feedback"] = "✅ Correct!"
        else:
            session["feedback"] = f"❌ Wrong! Correct Answer: {questions[session['questions'][q_index]]}"

    game_over = q_index >= 5
    question = session["questions"][q_index] if not game_over else None

    return render_template_string(
        template,
        question=question,
        q_num=q_index + 1,
        feedback=session.get("feedback", ""),
        game_over=game_over,
        score=session.get("score", 0)
    )

@app.route("/next", methods=["POST"])
def next_question():
    session["q_index"] += 1
    session["feedback"] = ""
    return redirect(url_for("index"))

@app.route("/restart", methods=["POST"])
def restart():
    session.clear()
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)



# uv run flask --app app run































# import streamlit as st
# import random

# questions = {
#     "Who developed Python programming language?": "Guido van Rossum",
#     "In which year was Python first released?": "1991",
#     "What is the file extension of a Python file?": ".py",
#     "What keyword is used to define a function in Python?": "def",
#     "Which keyword is used to create a class in Python?": "class",
#     "What is the output of print(type(10))?": "<class 'int'>",
#     "What data type is the result of 3 / 2 in Python 3?": "float",
#     "Which function is used to get the length of a list in Python?": "len()",
#     "What is the output of bool(\"\")?": "False",
#     "Which operator is used for exponentiation in Python?": "**",
#     "What keyword is used to handle exceptions in Python?": "try and except",
#     "Which built-in function is used to convert a string to an integer?": "int()",
#     "What is the correct syntax to import a module named math?": "import math",
#     "What is the output of print(\"Hello\" * 3)?": "HelloHelloHello",
#     "Which keyword is used to exit a loop in Python?": "break",
#     "What is the difference between is and == in Python?": "== checks values, is checks identity (memory address)",
#     "Which function is used to read input from the user?": "input()",
#     "What is the default value of the end parameter in the print() function?": "\\n",
#     "Which Python data type is mutable: tuple or list?": "list",
#     "What does PEP stand for in Python?": "Python Enhancement Proposal"
# }

# st.title("🐍 Python Trivia Game")

# # initialize session state
# if "score" not in st.session_state:
#     st.session_state.score = 0
#     st.session_state.q_index = 0
#     st.session_state.show_result = False
#     st.session_state.questions = random.sample(list(questions.keys()), 5)

# if st.session_state.q_index < len(st.session_state.questions):
#     question = st.session_state.questions[st.session_state.q_index]
#     st.write(f"**Q{st.session_state.q_index+1}: {question}**")
#     answer = st.text_input("Your Answer:")

#     if st.button("Submit") and not st.session_state.show_result:
#         if answer.strip().lower() == questions[question].lower():
#             st.success("✅ Correct!")
#             st.session_state.score += 1
#         else:
#             st.error(f"❌ Wrong! Correct Answer: {questions[question]}")
#         st.session_state.show_result = True

#     # Next Question button after showing result
#     if st.session_state.show_result:
#         if st.button("Next Question"):
#             st.session_state.q_index += 1
#             st.session_state.show_result = False
#             st.rerun()
# else:
#     st.write("🎉 **Game Over!**")
#     st.write(f"Your final score: **{st.session_state.score}/5**")
#     if st.button("Play Again"):
#         st.session_state.clear()
#         st.rerun()
