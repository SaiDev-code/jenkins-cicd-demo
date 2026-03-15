print("Hello from Jenkins CI/CD pipeline")

# app.py
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello from Jenkins CI/CD pipeline"

if __name__ == '__main__':
    # Make sure to bind to 0.0.0.0 so Docker can access it
    app.run(host='0.0.0.0', port=5000)
    