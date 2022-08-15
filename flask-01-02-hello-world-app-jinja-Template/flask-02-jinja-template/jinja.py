from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World from Flask!!!'
    
@app.route('/second')
def second():
    return 'Group Penguins!!!'


if __name__== "__main__":
    app.run(debug=True,port=2000)