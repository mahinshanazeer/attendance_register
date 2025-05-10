from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    try:
        data = request.get_json()
        if not data or 'query' not in data:
            return jsonify({"error": "Invalid request. JSON body with 'query' field expected."}), 400
        
        user_query = data.get('query')
        
        # TODO: Replace with actual Ollama and internet fetching logic
        bot_response = f"Backend received: '{user_query}'. This is a mock reply from the bot."
        
        return jsonify({"response": bot_response})

    except Exception as e:
        # Log the exception for debugging
        app.logger.error(f"Error in /chat endpoint: {e}")
        return jsonify({"error": "An internal server error occurred."}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000) # Specifying port for clarity, default is 5000
