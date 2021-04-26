# import dependencies
from flask import Flask

# create new flask instance called app
app = Flask(__name__)

# Add route
@app.route('/')
def hello_world():
    return 'Hello world'