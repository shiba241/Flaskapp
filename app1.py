from flask import Flask

app=Flask(__name__)

@app.route("/add/<n1>/<n2>")
def add(n1,n2):
    n3=int(n1)+int(n2)
    output=f'''<body bgcolor=yellow>
<h2>Sum of {n1} and {n2} is {n3}</h2>
</body>'''
    return output
    
    
app.run()

