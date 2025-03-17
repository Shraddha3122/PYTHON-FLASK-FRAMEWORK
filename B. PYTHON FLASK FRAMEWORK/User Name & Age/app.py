# Develop a Flask app with a form that accepts a user's name and age. 
# On submission, display a message like "Hello [name], you are [age] years old!" 
#on a separate page.

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    age = request.form['age']
    return render_template('result.html', name=name, age=age)

if __name__ == '__main__':
    app.run(debug=True)