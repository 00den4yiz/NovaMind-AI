import os
from flask import Flask, request, jsonify
from openai import OpenAI

app = Flask(__name__)
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

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
    except:
        return jsonify({"response": "Hata oluştu"})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

import os

from dotenv import load_dotenv
load_dotenv("/etc/secrets/.env")  # Eğer dosya buradaysa

api_key = os.environ.get("OPENAI_API_KEY")
