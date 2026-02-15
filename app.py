# app.py
import os
import redis
from flask import Flask, request, render_template
import joblib
import numpy as np

app = Flask(__name__)

# Load the pre-trained model
model_payload = joblib.load('iris_model.pkl')
model = model_payload['model']
target_names = model_payload['target_names']

# Connect to Redis
redis_host = os.environ.get('REDIS_HOST', 'localhost')
r = redis.Redis(host=redis_host, port=6379, db=0, decode_responses=True)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/health')
def health():
    return "OK", 200

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get data from the form
        sepal_length = float(request.form['sepal_length'])
        sepal_width = float(request.form['sepal_width'])
        petal_length = float(request.form['petal_length'])
        petal_width = float(request.form['petal_width'])

        # Create a numpy array for the model
        features = np.array([[sepal_length, sepal_width, petal_length, petal_width]])

        # Make prediction
        prediction_index = model.predict(features)[0]
        prediction_name = target_names[prediction_index]

        # Increment prediction counter in Redis
        count = r.incr('predictions')

        return render_template(
            'result.html',
            prediction=prediction_name,
            count=count
        )

    except Exception as e:
        return render_template('result.html', error=str(e))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
