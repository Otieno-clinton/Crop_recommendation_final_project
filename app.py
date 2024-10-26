from flask import Flask, request, render_template
import numpy as np
import pickle

model = pickle.load(open('model.pkl', 'rb'))
sc = pickle.load(open('minmaxscaler.pkl', 'rb'))
mx = pickle.load(open('standscaler.pkl', 'rb'))

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route("/predict", methods=['POST'])
def predict():
    try:
        # Convert input values to floats
        N = float(request.form['Nitrogen'])
        P = float(request.form['Phosporus'])
        K = float(request.form['Potassium'])
        temp = float(request.form['Temperature'])
        humidity = float(request.form['Humidity'])
        ph = float(request.form['pH'])
        rainfall = float(request.form['Rainfall'])

        # Prepare input features
        feature_list = [N, P, K, temp, humidity, ph, rainfall]
        single_pred = np.array(feature_list).reshape(1, -1)

        # Apply scaling transformations in the correct order
        mx_features = mx.transform(single_pred)  # First, apply mx scaler if intended
        sc_mx_features = sc.transform(mx_features)  # Then apply min-max scaler

        # Predict using the model
        prediction = model.predict(sc_mx_features)

        # If prediction is already a crop name, use it directly
        crop = prediction[0]  # Assume the model outputs the crop name directly
        result = f"{crop} is the best crop to be cultivated right there."

    except Exception as e:
        result = f"An error occurred during prediction: {e}"

    return render_template('index.html', result=result)


if __name__ == "__main__":
    app.run(debug=True)
