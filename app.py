import pickle
from flask import Flask, request, jsonify, render_template
import numpy as np
import pandas as pd

# Initialize Flask App
app = Flask(__name__)

# Load the model and scaler
regmodel = pickle.load(open('regmodel.pkl', 'rb'))
scalar = pickle.load(open('scaling.pkl', 'rb'))

# Home Route
@app.route('/')
def home():
    return render_template('home.html')


# API Route for Postman Testing
@app.route('/predict_api', methods=['POST'])
def predict_api():
    data = request.json['data']

    new_data = scalar.transform(
        np.array(list(data.values())).reshape(1, -1)
    )

    output = regmodel.predict(new_data)

    return jsonify(float(output[0]))


# HTML Form Prediction Route
@app.route('/predict', methods=['POST'])
def predict():
    data = [float(x) for x in request.form.values()]

    final_input = scalar.transform(
        np.array(data).reshape(1, -1)
    )

    output = regmodel.predict(final_input)

    return render_template(
        'home.html',
        prediction_text="The House price prediction is {}".format(output[0])
    )


# DEBUG ROUTE
@app.route('/routes')
def routes():
    return str(app.url_map)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)