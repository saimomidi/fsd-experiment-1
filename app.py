from flask import Flask

# Initialize the Flask app
app = Flask(__name__)

# Define a route for the home page
@app.route('/')
def home():
    return "Hello, World!"

# Run the app with the default Flask development server
if __name__ == '__main__':
    app.run(debug=True)

