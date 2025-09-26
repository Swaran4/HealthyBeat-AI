from flask import Flask, request, render_template
from model import predict

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict_route():
    try:
        # Get 10 numeric features from form based on index.html names
        input_data = [
            float(request.form['age']),
            float(request.form['gender']),
            float(request.form['cp']),
            float(request.form['trestbps']),
            float(request.form['chol']),
            float(request.form['fbs']),
            float(request.form['restecg']),
            float(request.form['thalach']),
            float(request.form['exang']),
            float(request.form['oldpeak'])
        ]

        # Make prediction using the model
        output = predict(input_data)

        return render_template('index.html', prediction_text=f'Prediction: {output}')

    except (KeyError, ValueError) as e:
        return "Error: Please fill all fields with valid numbers.", 400
    except Exception as e:
        return f"Error: {e}"

if __name__ == '__main__':
    app.run(debug=True)