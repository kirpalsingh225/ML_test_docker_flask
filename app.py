from flask import Flask, request, jsonify
import pickle
import numpy as np

# Load model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

# Create Flask app
app = Flask(__name__)

@app.route("/")
def home():
    return "Flask app is running!"

@app.route("/predict", methods=["GET", "POST"])
def predict():
    if request.method == "GET":
        # Optional: Predict using sample input or show a message
        sample_input = [5.1, 3.5, 1.4, 0.2]
        input_data = np.array(sample_input).reshape(1, -1)
        prediction = model.predict(input_data)
        return jsonify({
            "message": "This is a demo GET request",
            "sample_input": sample_input,
            "predicted_class": int(prediction[0])
        })

    # Handle POST request
    data = request.get_json()
    if not data or "data" not in data:
        return jsonify({"error": "Missing 'data' key in JSON body"}), 400

    try:
        input_data = np.array(data["data"]).reshape(1, -1)
        prediction = model.predict(input_data)
        return jsonify({
            "input": data["data"],
            "predicted_class": int(prediction[0])
        })
    except Exception as e:
        return jsonify({"error": f"Prediction failed: {str(e)}"}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
