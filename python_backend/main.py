# import flask to create the web app
from flask import Flask, request, jsonify
# import fizz_buzz_functions.py
import fizz_buzz_functions

#create flask app
app = Flask(__name__)

#create route and initialise the server
@app.route("/")
def test_server():
    return "Hello World"

#extract second function from fizz_buzz_functions.py, store in variable
add_nums_to_json = fizz_buzz_functions.add_nums_to_json
added_nums_list = add_nums_to_json(100)

#create route for numbers
@app.route("/api/numbers", methods = ["GET"])
def get_nums():
    print("nums: ", added_nums_list) # test
    if (len(added_nums_list)==0): #if list is empty
        return "No numbers found", 404 #return that no numbers are found
    return jsonify(added_nums_list), 200 #else return populated list in json format

#run the server
if __name__ == "__main__":
    app.run(debug=True)