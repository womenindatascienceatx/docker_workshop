from flask import Flask, render_template
import random
import pickle
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
app = Flask(__name__)

# list of cat images
images = []
digits = load_digits()
x_train, x_test, y_train, y_test = train_test_split(digits.data, digits.target, test_size=0.25, random_state=0)
loaded_model = pickle.load(open("model/logreg_model.pkl", 'rb'))

@app.route('/')
def index():
    prediction = loaded_model.predict(x_test[100].reshape(1,-1))
    static_image = "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e7/Friendly_pumpkin.jpg/128px-Friendly_pumpkin.jpg"
    # static_image = random.choice(image)
    # prediction = model.predict_emotion(static_image)
    return render_template('index.html', static_image=static_image, pred = prediction )

if __name__ == "__main__":
    app.run(host="0.0.0.0")
