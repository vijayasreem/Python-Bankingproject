Here is an example of Python Flask API code for the given User story:

```python
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/loan/verification', methods=['POST'])
def verify_loan_eligibility():
    # Get the loan application details from the request
    loan_application = request.json
    
    # Perform document verification
    identification_verified = verify_identification(loan_application['identification'])
    income_verified = verify_proof_of_income(loan_application['proof_of_income'])
    credit_history_verified = verify_credit_history(loan_application['credit_history'])
    employment_details_verified = verify_employment_details(loan_application['employment_details'])
    
    # Assess loan eligibility
    is_eligible = assessment_process(identification_verified, income_verified, credit_history_verified, employment_details_verified)
    
    # Generate eligibility report
    report = generate_report(is_eligible)
    
    # Notify bank employee
    notify_employee(report)
    
    return jsonify(report), 200

def verify_identification(identification):
    # Logic to verify identification documents
    return True

def verify_proof_of_income(proof_of_income):
    # Logic to verify proof of income documents
    return True

def verify_credit_history(credit_history):
    # Logic to verify credit history documents
    return True

def verify_employment_details(employment_details):
    # Logic to verify employment details documents
    return True

def assessment_process(identification_verified, income_verified, credit_history_verified, employment_details_verified):
    # Logic to assess loan eligibility based on verified documents
    if identification_verified and income_verified and credit_history_verified and employment_details_verified:
        return True
    else:
        return False

def generate_report(is_eligible):
    # Logic to generate eligibility report
    report = {
        'eligibility_status': 'Eligible' if is_eligible else 'Not Eligible'
    }
    return report

def notify_employee(report):
    # Logic to notify bank employee
    print('Eligibility Status:', report['eligibility_status'])

if __name__ == '__main__':
    app.run()
```

In this code, we define a Flask API endpoint `/loan/verification` which accepts a POST request. The loan application details are extracted from the request, and then the document verification and loan eligibility assessment processes are performed. Finally, a report is generated and the bank employee is notified.