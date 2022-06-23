from flask import Flask, render_template, request
# import jsonpify
# flask.jsonpify()
import requests
import pickle
import numpy as np
import sklearn
from sklearn.preprocessing import StandardScaler
app = Flask(__name__)
model = pickle.load(open('linear_model.pkl', 'rb'))
@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')
['Head Size(cm^3)']

standard_to = StandardScaler()
@app.route("/predict", methods=['POST'])
def predict():
    if request.method == 'POST':
        print(request)
        Head_Size = int(request.form['Head Size(cm^3)'])
        output=model.predict([[Head_Size]])[0][0]
        return render_template('index.html',prediction_text="Your brain weight is {} gram".format(output))
    else:
        return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)