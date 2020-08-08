# Main Script

from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('about.html',title='About')

@app.route('/about')
def about():
    return "<H1> About Page </H1>"


if __name__ == "__main__":
    app.run(debug=True)