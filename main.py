from flask import Flask, request, render_template
import requests
import json

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', answer=None)

@app.route('/get_response', methods=['POST'])
def get_response():
    input_text = request.form['user_input']
    answer = get_chatgpt_response(input_text)
    return render_template('index.html', answer=answer, user_input=input_text)

def get_chatgpt_response(input_text):
    endpoint = "https://api.openai.com/v1/chat/completions"
    headers = {
        "Authorization": "Bearer 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",
        "Content-Type": "application/json"
    }
    data = {
        "model": "gpt-3.5-turbo",
        "messages": [{"role": "system", "content": "You are a helpful assistant."},
                     {"role": "user", "content": input_text}]
    }

    response = requests.post(endpoint, headers=headers, json=data)
    response_data = json.loads(response.text)
    return response_data['choices'][0]['message']['content']

if __name__ == '__main__':
    app.run(debug=True)