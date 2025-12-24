from flask import Flask, request, jsonify, render_template
import os
from openai import OpenAI

app = Flask(__name__)
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Ana sayfa: index.html dosyasını render eder
@app.route("/")
def home():
    return render_template("index.html")

# Chat endpoint: kullanıcı mesajını alır, OpenAI'dan cevap döndürür
@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    message = data.get("message", "").strip()

    if not message:
        return jsonify({"response": "Soru algılanamadı"})

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": message}]
        )
        resp_text = response.choices[0].message.content if response.choices else "Cevap alınamadı"
        return jsonify({"response": resp_text})
    except Exception as e:
        print("Hata:", e)
        return jsonify({"response": "Cevap alınamadı"})

if __name__ == "__main__":
    app.run(debug=True)
