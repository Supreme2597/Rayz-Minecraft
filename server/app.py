# server/app.py
from flask import Flask, request, jsonify
import openai, os

openai.api_key = os.getenv('OPENAI_API_KEY')
app = Flask(__name__)

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    user = data['user']
    msg = data['message']
    
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are Rayz, an AI bot that lives inside Minecraft."},
            {"role": "user", "content": f"{user} said: {msg}"}
        ]
    )

    return jsonify({'reply': response.choices[0].message['content']})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
