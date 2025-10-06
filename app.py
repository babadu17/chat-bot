from flask import Flask, render_template, request, jsonify
import openai
import os

app = Flask(__name__)

openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    user_message = request.json["message"]

    # Appel à GPT
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # ou "gpt-4" si tu veux
        messages=[
            {"role": "system", "content": "Tu es un chatbot sympathique qui aide les utilisateurs."},
            {"role": "user", "content": user_message}
        ]
    )

    bot_reply = response["choices"][0]["message"]["content"]
    return jsonify({"reply": bot_reply})

if __name__ == "__main__":
    app.run(debug=True)
