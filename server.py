import os
from flask import Flask, request, render_template
import requests
import test

app = Flask(__name__)

@app.route('/handle_form', methods=['POST'])
def handle_form():
    print("Posted file: {}".format(request.files['file']))
    f = request.files['file']  
    f.save("uploaded_images/"+f.filename)
    sample_image = "uploaded_images/" + f.filename
    result = test.predict_disease(sample_image)
    return render_template("success.html",name=f.filename, result1=result);



@app.route("/")
def index():
    return render_template("index.html");   


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8080, debug=True, threaded = False)
