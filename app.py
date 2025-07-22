
from flask import Flask, render_template
from fbref_scraper import get_predictions

app = Flask(__name__)

@app.route('/')
def home():
    predictions = get_predictions()
    return render_template('index.html', predictions=predictions)

if __name__ == '__main__':
    app.run(debug=True)
