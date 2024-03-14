Here is a basic example of a Python Flask API code for the given user story:

```python
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/apply', methods=['POST'])
def apply_loan():
    data = request.get_json()
    
    # Validate the entered information
    if not data.get('name') or not data.get('email') or not data.get('phone') or not data.get('address'):
        return jsonify({'error': 'Missing required information'}), 400
    
    # Process the loan application
    # ...
    # Save the application data to the database
    
    return jsonify({'message': 'Loan application submitted successfully'}), 200

if __name__ == '__main__':
    app.run(debug=True)
```

This is a basic Flask API with a single route `/apply` that accepts POST requests. The request data is expected to be in JSON format.

The code checks if the required information (name, email, phone, and address) is present in the request data. If any of the required fields are missing, it returns a JSON response with an error message and a status code of 400 (Bad Request). Otherwise, it processes the loan application, saves the data to the database, and returns a JSON response with a success message and a status code of 200 (OK).

Please note that this is just a basic example and you would need to further develop the code to meet all the acceptance criteria and implement the desired features.