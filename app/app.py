Sure! Here's an example of a Python Flask API code that can handle the car mortgage loan application process through multiple channels:

```python
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/loan_application', methods=['POST'])
def loan_application():
    data = request.json

    # Validate required fields
    if not data.get('personal_details') or not data.get('income_information') or not data.get('employment_details'):
        return jsonify({'error': 'Missing required fields'}), 400

    # Save application data to database
    # Your code to save the application data to the database goes here

    return jsonify({'message': 'Loan application submitted successfully'}), 200

if __name__ == '__main__':
    app.run(debug=True)
```

This code defines a Flask API with a single route `/loan_application` that accepts a POST request to submit a loan application. The request should include a JSON payload with the necessary information, including personal details, income information, and employment details.

The code validates the presence of these required fields and returns an error message if any are missing. If all the required fields are present, you can add your own code to save the application data to a database.

You can run this Flask API using `python app.py` and it will start a local server. You can then send a POST request to `http://localhost:5000/loan_application` with the loan application data in the JSON payload.

Please note that this is just a basic example and you'll need to add more code to handle the additional acceptance criteria, such as saving progress, providing clear instructions, validating data, and providing contact information or customer support options.