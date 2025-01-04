from flask import Flask, request, jsonify, render_template
import openai
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allow Cross-Origin Resource Sharing for frontend-backend communication

# Set your OpenAI API key
openai.api_key = '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'

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message', '').strip()
    if not user_message:
        return jsonify({'reply': "Sorry, I didn't understand. Can you rephrase?"})

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant designed to assist Tuhin's portfolio website visitors."},
                {"role": "user", "content": user_message}
            ]
        )
        reply = response['choices'][0]['message']['content'].strip()
        return jsonify({'reply': reply})
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({'reply': "Oops, something went wrong. Please try again later."})

if __name__ == '__main__':
    app.run(debug=True)
