# import flask to create the web app
from flask import Flask, request, jsonify

#create flask app
app = Flask(__name__)

#create route and initialise the server
@app.route("/")
def test_server():
    return "Hello World"

#run the server
if __name__ == "__main__":
    app.run(debug=True)