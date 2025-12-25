from flask import Flask, request, jsonify
import openai
import os

app = Flask(__name__)

# OpenAI API key Render Secret Files / Environment Variable ile
openai.api_key = os.environ.get("OPENAI_API_KEY")

@app.route("/ask", methods=["POST"])
def ask():
    data = request.get_json()
    question = data.get("question", "").strip()
    
    if not question:
        return jsonify({"reply": "Hata: Soru boş olamaz."})
    
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": question}],
            max_tokens=300
        )
        answer = response.choices[0].message.content
        return jsonify({"reply": answer})
    except Exception as e:
        return jsonify({"reply": f"Hata oluştu: {str(e)}"})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
