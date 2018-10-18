from flask import Flask, render_template
import random

app = Flask(__name__)

# list of cat images
images = []
# model = FacialExpressionModel()
@app.route('/')
def index():
    static_image = "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e7/Friendly_pumpkin.jpg/128px-Friendly_pumpkin.jpg"
    # static_image = random.choice(image)
    # prediction = model.predict_emotion(static_image)
    return render_template('index.html', static_image=static_image )

if __name__ == "__main__":
    app.run(host="0.0.0.0")
