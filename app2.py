from flask import Flask,render_template

app=Flask(__name__)
@app.route('/index')
def index():
    output=render_template("index.html")
    return output

app.run()
