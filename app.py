from flask import Flask, jsonify
from flask import Flask, redirect, render_template, request, session, url_for
import requests

import json
import yaml

app = Flask(__name__)

# @app.route("/")
# def hello():
#     return render_template("index.html")
@app.route("/get_cwl", methods=["GET", "POST"])
def parametertest():
    url = "missing URL"
    label = "missing label"
    hasError = True
    if request.method == "POST":
        url = request.form['url']
        r = requests.get(url, allow_redirects=True)
        obj = yaml.safe_load(r.content)
        print(len(obj['inputs']))
        print(len(obj['outputs']))
        if 'label' in obj:
            label = obj['label']

        hasError = False
        
    return jsonify({'error' : hasError,'url' : url, 'label':label,'input': len(obj['inputs']), 'output': len(obj['outputs'])})

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)