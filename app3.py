from flask import Flask,render_template

app=Flask(__name__)

@app.route("/add/<int:n1>/<int:n2>")
def add(n1,n2):
    n3=n1+n2
    output=render_template("add_temp.html",n1=n1,n2=n2,n3=n3)
    return output

app.run()
