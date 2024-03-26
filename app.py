from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World from -- nathanjh-28 -- in 3308'
