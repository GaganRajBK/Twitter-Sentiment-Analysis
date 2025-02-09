
from flask import Flask, request, render_template
import joblib

app = Flask(__name__)

# Load the pre-trained logistic regression model and vectorizer
model_path = 'logistic_model.sav'
vectorizer_path = 'vectorizer.sav'
vectorizer = joblib.load(vectorizer_path)
model = joblib.load(model_path)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        message = request.form['message']
        data = vectorizer.transform([message])  # Transform the input text to the expected format
        prediction = model.predict(data)
        sentiment = 'Positive 😊' if prediction[0] == 1 else 'Negative 😔'
        return render_template('result.html', prediction=sentiment)

if __name__ == '__main__':
    app.run(debug=True)

