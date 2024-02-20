Sure! Here's an example of Python Flask API code that implements the loan application status check functionality based on the given user story:

```python
from flask import Flask, request, jsonify

app = Flask(__name__)

# Mock database of loan applications
loan_applications = [
    {
        'id': '1',
        'email': 'john@example.com',
        'status': 'Pending',
    },
    {
        'id': '2',
        'email': 'jane@example.com',
        'status': 'Approved',
    },
    # Add more loan applications here
]

# Route for loan application status check
@app.route('/loan-application/status', methods=['POST'])
def check_loan_application_status():
    loan_id = request.json['loan_id']
    otp = request.json['otp']

    # Retrieve loan application details from the database
    loan_application = next((app for app in loan_applications if app['id'] == loan_id), None)

    if not loan_application:
        return jsonify({'error': 'Loan application not found'}), 404

    # Check if the entered OTP matches the one generated and sent to the applicant
    if otp != generate_and_send_otp(loan_application['email']):
        return jsonify({'error': 'Invalid OTP'}), 400

    return jsonify({'status': loan_application['status']}), 200

# Function to generate and send OTP to the applicant's email address
def generate_and_send_otp(email):
    # Implement OTP generation and email sending logic securely and robustly
    # This is a mock implementation for demonstration purposes
    return '1234'  # Replace with actual OTP generation and email sending logic

if __name__ == '__main__':
    app.run(debug=True)
```

Note: This code is a simplified example and does not include the actual implementation of OTP generation and email sending logic. You would need to replace the `generate_and_send_otp` function with your own implementation to generate a random OTP and send it securely using Salesforce's email functionality.

To run the Flask API, save the code in a file named `app.py` and execute the following command in your terminal:

```
python app.py
```

The API will be accessible at http://localhost:5000/loan-application/status and can be tested using a tool like Postman by sending a POST request with the loan ID and OTP in the request body as JSON data.