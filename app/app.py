Sure! Here's an example of a Python Flask API code that provides convenient options for car mortgage loan applications:

```python
from flask import Flask, request

app = Flask(__name__)

@app.route('/apply', methods=['POST'])
def apply_loan():
    data = request.get_json()
    
    # Process the loan application based on the requested channel
    channel = data.get('channel', '')
    if channel == 'in-person':
        # Handle in-person loan application
        return "Thank you for applying in-person. Your loan application is being processed."
    elif channel == 'website':
        # Handle website loan application
        return "Thank you for applying through the website. Your loan application is being processed."
    elif channel == 'mobile':
        # Handle mobile app loan application
        return "Thank you for applying through the mobile app. Your loan application is being processed."
    else:
        return "Invalid channel. Please choose from in-person, website, or mobile app."

if __name__ == '__main__':
    app.run(debug=True)
```

In this code, we define a Flask API with a single endpoint `/apply` that accepts POST requests. The loan application details are expected to be sent in the request body as JSON data.

The API checks the `channel` value from the request data and processes the loan application accordingly. If the channel is 'in-person', 'website', or 'mobile', it returns a corresponding success message. If the channel is not one of these options, it returns an error message.

You can run this code and test the API using tools like Postman or by sending a POST request to `http://localhost:5000/apply` with the JSON data containing the channel information.