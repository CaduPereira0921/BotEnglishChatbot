from flask import Flask, request, jsonify, render_template
from botenglish_chatbot import BotEnglishChatbot

app = Flask(__name__)
bot = BotEnglishChatbot()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    mensagem = request.json.get("message", "")
    resposta = bot.processar_pergunta(mensagem)
    return jsonify({"response": resposta})

if __name__ == "__main__":
    app.run(debug=True)
