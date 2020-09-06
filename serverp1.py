#!flask/bin/python
from flask import Flask, request, jsonify
#import test
import os
app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello From Server"

@app.route('/upload', methods=['POST'])
def upload():
    if request.method == 'POST':  
        print("Posted file: {}".format(request.files['file']))
        file = request.files['file']
        return ""  
    else:
        return "Error \n\n\n"

#@app.route('/sensor-data', methods=['POST'])
#def sensorData():
#    if (request.is_json):
#        content = request.get_json()
#        
#        print(content["A"])
#        print(content["B"])
#        print(sample(content["A"],content["B"]))
#
#        return "\nOk\n\n\n"
#    else:
#        return "Error \n\n\n"

if __name__ == '__main__':
    app.run(debug=True, port=4000)

