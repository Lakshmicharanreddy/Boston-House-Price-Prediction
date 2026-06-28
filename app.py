import pickle
from flask import Flask,request,app,jsonify,url_for,render_template


import numpy as np
import pandas as pd

# 1. Initialize the Flask App
app = Flask(__name__)

# 2. Load the pickled regression model and the standard scalar

regmodel = pickle.load(open('regmodel.pkl', 'rb'))
scalar = pickle.load(open('scaling.pkl', 'rb'))

#Define home page Router

@app.route('/')
def home():
    return render_template('home.html')

# 4. Define the predict API route (for testing with tools like Postman)

@app.route('/predict_api',methods=['POST'])

def predict_api():
    data = request.json['data']
    print(data)
    print(np.array(list(data.values())).reshape(1,-1))
    new_data = scalar.transform(np.array(list(data.values())).reshape(1,-1))
    output = regmodel.predict(new_data)
    print(output[0])
    return jsonify(output[0])


# 5. Define the predict route (for the HTML web form)
@app.route('/predict', methods=['POST'])
def predict():
    # Capture all input values from the HTML form and convert them to floats
    data = [float(x) for x in request.form.values()]
    
    # Reshape and standardize the input array
    final_input = scalar.transform(np.array(data).reshape(1, -1))
    print(final_input)
    
    # Predict the house price
    output = regmodel.predict(final_input)
    
    # Return the prediction back to the home.html placeholder
    return render_template('home.html', prediction_text="The House price prediction is {}".format(output))


if __name__ == "__main__":
    app.run(debug=True)