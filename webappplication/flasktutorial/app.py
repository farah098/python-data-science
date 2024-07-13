# flask is a module
# inside this module we have a class called Flask
# Let us import class "Flask"
from flask import Flask

# Let us create an instance of object of the class Flask
# The Flask class has __init__(constructor) method
# The constructor takes the file which is going to be the main program
# as parameter
# In other words, we are saying app.py is the main program
app = Flask(__name__)

# print(__name__)

# if anybody make http request for "/" then execute
# the following function
# which return Hello World!! we can see that in the browser
@app.route("/")
def say_hello():
    return "hello World!!!"

@app.route("/products")
def get_products():
    return ["apple","orange","mango"]