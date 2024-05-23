import sys
import os

# Add the path to the 'utils' folder to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'utils')))

# Now you can import the module from the 'utils' folder
from utils import logic
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/process_input', methods=['POST'])
def process_input():
    input_data = request.form['input_data']
    # Process the input data here (e.g., call your logic function)
    # For demonstration purposes, let's just return the processed data as uppercase
    processed_result = input_data
    final_result = logic.samoosa(processed_result)
    # Log the response to the console
    print('Response:', final_result)

    return jsonify({'result': final_result})


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=4000)
