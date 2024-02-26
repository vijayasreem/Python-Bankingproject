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

