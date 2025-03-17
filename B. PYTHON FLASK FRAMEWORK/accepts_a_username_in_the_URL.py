#Build a Flask app that accepts a username in the URL 
#(e.g., /hello/<username>) and displays a personalized greeting like "Hello, [username]!".


from flask import Flask

app = Flask(__name__)

@app.route('/hello/<username>')
def hello_user(username):
    return f'Hello, {username}!'

if __name__ == '__main__':
    app.run(debug=True)