import os
from flask import Flask, request, jsonify
import openai
from dotenv import load_dotenv

# .env dosyasını yükle (Render'da /etc/secrets/.env kullanabilirsin)
load_dotenv("/etc/secrets/.env")  # Eğer local çalıştırıyorsan load_dotenv() yeterli

# OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

# Flask uygulaması
app = Flask(__name__)

@app.route("/ask", methods=["POST"])
def ask():
    """
    Kullanıcı sorusunu alır ve OpenAI API ile yanıt döner.
    JSON formatında POST edilmeli:
    { "question": "Merhaba, nasılsın?" }
    """
    try:
        data = request.get_json()
        question = data.get("question", "")
        
        if not question:
            return jsonify({"answer": "Lütfen bir soru gönderin."})
        
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=question,
            max_tokens=150,
            temperature=0.7
        )
        
        answer = response.choices[0].text.strip()
        return jsonify({"answer": answer})
    
    except Exception as e:
        return jsonify({"answer": f"Hata oluştu: {str(e)}"})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    # Render’da mutlaka 0.0.0.0 host kullan
    app.run(host="0.0.0.0", port=port)

