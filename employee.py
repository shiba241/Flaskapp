
from flask_mysqldb import MySQL 
from flask import Flask,render_template,request 

app=Flask(__name__)

app.config['MYSQL_HOST']="localhost"
app.config['MYSQL_USER']="root"
app.config['MYSQL_PASSWORD']="1452"
app.config['MYSQL_DB']="database4"

mysql=MySQL(app)

@app.route("/addemp",methods=["GET","POST"])
def addemp():
    if request.method=="GET":
        response=render_template("addemp_temp.html")
        return response 
    elif request.method=="POST":
        empno=int(request.form['empno'])
        ename=request.form['ename']
        job=request.form['job']
        sal=float(request.form['sal'])
        c=mysql.connection.cursor()
        cmd="insert into emp values(%s,%s,%s,%s)"
        c.execute(cmd,(empno,ename,job,sal))
        mysql.connection.commit()
        response=render_template("home.html",msg="Employee Created...")
        return response 
@app.route("/home")
def home():
    response=render_template("home.html")
    return response

@app.route("/listemp")
def listemp():
    c=mysql.connection.cursor()
    c.execute("select * from emp")
    rows=c.fetchall()
    response=render_template("listemp.html",emp=rows)
    return response

@app.route("/updateemp",methods=["GET","POST"])
def updateemp():
    if request.method=="GET":
        response=render_template("updateemp_temp.html")
        return response
    elif request.method=="POST":
        empno=int(request.form['empno'])
        sal=float(request.form['sal'])
        c=mysql.connection.cursor()
        c.execute("update emp set salary=salary+%s where empno=%s",(sal,empno))
        k=c.rowcount
        if k==0:
            msg="Invalid EmployeeNo" 
        else:
            msg="Salary Updated"
            mysql.connection.commit()
        response=render_template("home.html",msg=msg)
        return response

@app.route("/delemp",methods=["GET","POST"])
def delemp():
    if request.method=="GET":
        response=render_template("delemp_temp.html")
        return response
    elif request.method=="POST":
        empno=int(request.form['empno'])
        c=mysql.connection.cursor()
        c.execute("delete from emp where empno=%s",(empno,))
        k=c.rowcount
        if k==0:
            msg="Invalid EmployeeNo"
        else:
            msg="Employee Deleted..."
            mysql.connection.commit()
        response=render_template("home.html",msg=msg)
        return response

app.run(debug=True)

