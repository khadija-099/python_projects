from flask import Flask, render_template_string, request
import string, random

app = Flask(__name__)

HTML_TEMPLATE = """
<!doctype html>
<html>
<head>
    <title>Password Generator</title>
</head>
<body style="font-family: Arial; margin: 50px;">
    <h2>🔐 Password Generator</h2>
    <form method="post">
        <label>Password Length:</label>
        <input type="number" name="length" min="4" value="12"><br><br>

        <label><input type="checkbox" name="uppercase"> Include Uppercase</label><br>
        <label><input type="checkbox" name="special"> Include Special Characters</label><br>
        <label><input type="checkbox" name="digits"> Include Digits</label><br><br>

        <button type="submit">Generate</button>
    </form>

    {% if password %}
        <h3>Generated Password:</h3>
        <p style="font-size:20px; font-weight:bold; color:green;">{{ password }}</p>
    {% endif %}
</body>
</html>
"""

def generate_password(length, uppercase, special, digits):
    lower = string.ascii_lowercase
    uppercase_chars = string.ascii_uppercase if uppercase else ""
    special_chars = string.punctuation if special else ""
    digit_chars = string.digits if digits else ""
    all_chars = lower + uppercase_chars + special_chars + digit_chars

    required = []
    if uppercase:
        required.append(random.choice(uppercase_chars))
    if special:
        required.append(random.choice(special_chars))
    if digits:
        required.append(random.choice(digit_chars))

    remaining = length - len(required)
    password = required + [random.choice(all_chars) for _ in range(remaining)]
    random.shuffle(password)
    return "".join(password)

@app.route("/", methods=["GET", "POST"])
def home():
    password = None
    if request.method == "POST":
        length = int(request.form["length"])
        uppercase = "uppercase" in request.form
        special = "special" in request.form
        digits = "digits" in request.form
        password = generate_password(length, uppercase, special, digits)
    return render_template_string(HTML_TEMPLATE, password=password)

if __name__ == "__main__":
    app.run(debug=True)



































# import streamlit as st
# import string
# import random

# st.title("🔐 Password Generator")

# length = st.number_input("Enter password length", min_value=1, max_value=50, value=12)
# include_uppercase = st.checkbox("Include Uppercase Letters")
# include_special = st.checkbox("Include Special Characters")
# include_digits = st.checkbox("Include Digits")

# if st.button("Generate Password"):
#     if length < 4:
#         st.error("❌ Password length should be at least 4 characters!")
#     else:
#         lower = string.ascii_lowercase
#         uppercase = string.ascii_uppercase if include_uppercase else ""
#         special = string.punctuation if include_special else ""
#         digits = string.digits if include_digits else ""
#         all_characters = lower + uppercase + special + digits

#         required_characters = []
#         if include_uppercase:
#             required_characters.append(random.choice(uppercase))
#         if include_special:
#             required_characters.append(random.choice(special))
#         if include_digits:
#             required_characters.append(random.choice(digits))

#         remaining_length = length - len(required_characters)
#         password = required_characters + [random.choice(all_characters) for _ in range(remaining_length)]

#         random.shuffle(password)
#         str_password = "".join(password)
#         st.success(f"✅ Your Password: {str_password}")
