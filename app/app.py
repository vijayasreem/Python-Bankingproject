Sure! Here's an example of how you can create a Python Flask API for the given User Story:

```python
from flask import Flask, jsonify, request

app = Flask(__name__)

# Store loan applications in memory (replace with a database in production)
loan_applications = []

# Route for submitting a loan application
@app.route('/loan-application', methods=['POST'])
def submit_loan_application():
    data = request.get_json()

    # Validate the required fields
    if not data.get('personal_details') or not data.get('income_information') or not data.get('employment_details'):
        return jsonify({'error': 'Incomplete application form'}), 400

    # Process the loan application
    loan_application = {
        'personal_details': data.get('personal_details'),
        'income_information': data.get('income_information'),
        'employment_details': data.get('employment_details')
    }
    loan_applications.append(loan_application)

    return jsonify({'message': 'Loan application submitted successfully'}), 200

# Route for retrieving all loan applications
@app.route('/loan-applications', methods=['GET'])
def get_loan_applications():
    return jsonify(loan_applications), 200

if __name__ == '__main__':
    app.run(debug=True)
```

This code sets up a basic Flask API with two routes. The `submit_loan_application` route handles the submission of a loan application form, validating the required fields and storing the application data in memory. The `get_loan_applications` route retrieves all the loan applications stored in memory.

You can customize and extend this code based on your specific requirements, such as adding additional validation, connecting to a database, or implementing authentication and authorization mechanisms.