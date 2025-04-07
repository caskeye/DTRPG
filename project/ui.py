# app.py
from flask import Flask, render_template, request, jsonify
# Assuming you have your LLM agent in a separate file/class
# from llm_agent import LLMAgent 

app = Flask(__name__)
# agent = LLMAgent() # Initialize your LLM agent

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/interact', methods=['POST'])
def interact():
    user_input = request.form['user_input']
    # llm_response = agent.get_response(user_input)
    llm_response = "Sample LLM response"
    return jsonify({'response': llm_response})

if __name__ == '__main__':
    app.run(debug=True)