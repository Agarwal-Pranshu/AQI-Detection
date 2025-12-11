from flask import Flask, render_template, request
import joblib
import pandas as pd

app = Flask(__name__)

# Load model
model = joblib.load("models/vote_model.joblib")

# Required features (same order as training)
numeric_features = ['PM2.5','PM10','NO','NO2','NOx','NH3','CO','SO2','O3']
categorical_features = ['City','State']
expected_columns = numeric_features + categorical_features


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Read form data
        form_data = {col: request.form.get(col) for col in expected_columns}

        # Convert numeric fields
        for col in numeric_features:
            form_data[col] = float(form_data[col])

        # Create dataframe for prediction
        input_df = pd.DataFrame([form_data], columns=expected_columns)

        # Predict
        predicted_aqi = model.predict(input_df)[0]

        return render_template(
            "index.html",
            prediction_text=f"Predicted AQI: {predicted_aqi:.2f}"
        )

    except Exception as e:
        return render_template(
            "index.html",
            prediction_text=f"Error: {str(e)}"
        )


if __name__ == "__main__":
    app.run(debug=True)
