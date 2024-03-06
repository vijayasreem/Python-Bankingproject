Here's a basic structure for a Python Flask API that can handle the car mortgage loan application process through multiple channels:

```python
from flask import Flask, request

app = Flask(__name__)

@app.route('/loan-application', methods=['POST'])
def submit_loan_application():
    # Retrieve loan application form data from the request
    loan_application_data = request.get_json()

    # Validate the loan application data
    validation_errors = validate_loan_application_data(loan_application_data)
    if validation_errors:
        return {'errors': validation_errors}, 400

    # Save the loan application data to a database or any other storage
    save_loan_application_data(loan_application_data)

    # Return a success message
    return {'message': 'Loan application submitted successfully'}, 200

def validate_loan_application_data(loan_application_data):
    errors = []

    # Validate personal details
    if 'name' not in loan_application_data:
        errors.append('Name is required')
    # Add more validation logic for personal details

    # Validate income information
    if 'income' not in loan_application_data:
        errors.append('Income is required')
    # Add more validation logic for income information

    # Validate employment details
    if 'employment' not in loan_application_data:
        errors.append('Employment details are required')
    # Add more validation logic for employment details

    # Add more validation logic for other fields

    return errors

def save_loan_application_data(loan_application_data):
    # Save the loan application data to a database or any other storage
    pass

if __name__ == '__main__':
    app.run(debug=True)
```

This code sets up a Flask API with a single route `/loan-application` that handles the submission of loan applications. The API expects the loan application data to be sent as a JSON object in the request body. The loan application data is then validated using the `validate_loan_application_data` function, which checks for the presence of required fields and performs any additional validation logic. If there are any validation errors, the API returns a response with the errors and a 400 status code. If the loan application data is valid, it is saved using the `save_loan_application_data` function, and a success message is returned with a 200 status code.

You can extend this code to include the remaining acceptance criteria, such as handling saving progress, displaying error messages, providing clear instructions, and adding dedicated sections or pages for loan applications on the bank's website and mobile app.